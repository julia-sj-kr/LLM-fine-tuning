import serial
import time

arduino_serial=serial.Serial('COM3',115200,timeout=1)

while True:
     for c in arduino_serial.read():
         print(chr(c),end='')
