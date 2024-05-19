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

def send_pwm_value(pin, value):
    command = f'{pin}:{value}\n'
    
    ser.write(command.encode())
 
   
if __name__ == "__main__":
    while True:
        send_pwm_value(3,a  )

        send_pwm_value(5, )
        
        send_pwm_value(6, )
        
        send_pwm_value(9, )

        send_pwm_value(10,)
        
        send_pwm_value(11, )

ser.close()
