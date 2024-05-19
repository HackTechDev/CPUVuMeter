#!/usr/bin/python3

import psutil

import serial
import time
import math
import shutil

serial_port = '/dev/ttyACM0'
baud_rate = 9600

ser = serial.Serial(serial_port, baud_rate)
time.sleep(2)

max_vumetre_0 = 150
max_vumetre_1 = 150
max_vumetre_2 = 150
max_vumetre_3 = 150
max_vumetre_4 = 150
max_vumetre_5 = 150

def get_network_load(interval=1):
    """Calculate network load in Kb/s."""
    # Get initial network I/O stats
    net_io_start = psutil.net_io_counters()

    # Sleep for the interval
    time.sleep(interval)

    # Get network I/O stats after the interval
    net_io_end = psutil.net_io_counters()

    # Calculate the difference and convert bytes to kilobytes
    bytes_sent = net_io_end.bytes_sent - net_io_start.bytes_sent
    bytes_recv = net_io_end.bytes_recv - net_io_start.bytes_recv

    kb_sent = bytes_sent / 1024
    kb_recv = bytes_recv / 1024

    return kb_sent, kb_recv


def get_cpu_load(cpu_number):
    cpu_loads = psutil.cpu_percent(interval=1,  percpu=True)
    specific_cpu_load = cpu_loads[cpu_number]
    return specific_cpu_load

def send_pwm_value(pin, value):
    command = f'{pin}:{value}\n'
    
    ser.write(command.encode())
 

def map_value(value, from_min, from_max, to_min, to_max):
    # Scale the value from the original range to a value between 0 and 1
    scaled_value = (value - from_min) / (from_max - from_min)
    
    # Map the scaled value to the new range
    mapped_value = to_min + (scaled_value * (to_max - to_min))
    
    return mapped_value
   
if __name__ == "__main__":
    while True:
        cpu_load_0 = get_cpu_load(0)
        cpu_vumetre_0 = math.ceil(map_value(cpu_load_0, 1, 100, 1, max_vumetre_0))
        print(f"CPU Load 0: {cpu_load_0}% <=> {cpu_vumetre_0}/{max_vumetre_0}")
        send_pwm_value(3, map_value(cpu_load_0, 1, 100, 1, max_vumetre_0))

        cpu_load_1 = get_cpu_load(1)
        cpu_vumetre_1 = math.ceil(map_value(cpu_load_1, 1, 100, 1, max_vumetre_1))
        print(f"CPU Load 1: {cpu_load_1}% <=> {cpu_vumetre_1}/{max_vumetre_1}")
        send_pwm_value(5, map_value(cpu_load_1, 1, 100, 1, max_vumetre_1))
        
        cpu_load_2 = get_cpu_load(2)
        cpu_vumetre_2 = math.ceil(map_value(cpu_load_2, 1, 100, 1, max_vumetre_2))
        print(f"CPU Load 2: {cpu_load_2}% <=> {cpu_vumetre_2}/{max_vumetre_2}")        
        send_pwm_value(6, map_value(cpu_load_2, 1, 100, 1, max_vumetre_2))
        
        cpu_load_3 = get_cpu_load(3)
        cpu_vumetre_3 = math.ceil(map_value(cpu_load_3, 1, 100, 1, max_vumetre_3))
        print(f"CPU Load 3: {cpu_load_3}% <=> {cpu_vumetre_3}/{max_vumetre_3}")        
        send_pwm_value(9, map_value(cpu_load_3, 1, 100, 1, max_vumetre_3))

        total, used, free = shutil.disk_usage("/")
        used_percentage = (used / total) * 100
        send_pwm_value(10, map_value(used_percentage, 1, 100, 1, max_vumetre_4))
        print(f"Disk usage: {used_percentage}%")   
        
        kb_sent, kb_recv = get_network_load()
        print(f"Kb sent: {kb_sent:.2f} Kb/s | Kb received: {kb_recv:.2f} Kb/s")
        send_pwm_value(11, map_value(kb_recv, 1, 1000, 1, max_vumetre_5))

ser.close()
