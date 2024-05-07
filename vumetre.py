#!/usr/bin/python3

import psutil

import serial
import time
import math

serial_port = '/dev/ttyACM0'
baud_rate = 9600

ser = serial.Serial(serial_port, baud_rate)
time.sleep(2)

max_vumetre = 150

def get_cpu_load():
    cpu_load = psutil.cpu_percent(interval=1)
    return cpu_load

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
        cpu_load = get_cpu_load()
        cpu_vumetre = math.ceil(map_value(cpu_load, 1, 100, 1, max_vumetre))
        print(f"CPU Load: {cpu_load}% <=> {cpu_vumetre}/{max_vumetre}")
        send_pwm_value(9, map_value(cpu_load, 1, 100, 1, max_vumetre))

ser.close()
