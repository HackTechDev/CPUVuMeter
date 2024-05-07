import serial
import time

serial_port = '/dev/ttyACM0'
baud_rate = 9600

ser = serial.Serial(serial_port, baud_rate)
time.sleep(2)

def send_pwm_value(pin, value):
    command = f'{pin}:{value}\n'
    
    ser.write(command.encode())

send_pwm_value(9, 75)

ser.close()

