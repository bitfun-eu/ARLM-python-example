# Please flash your microbit with an *EMPTY* script first!
# And change your COMx port accordingly
from time import sleep
from serial import Serial
#from serial import *
from serial.tools.list_ports import comports

if comports:
    port_list = list(comports())
    for port in port_list:
        print(port[0])
        print(port[1])
        print(port[2])

MBIT = Serial('COM3', baudrate=115200, timeout=1)

def line(s):
    cmd = s + '\r\n'
    cmd = cmd.encode()
    MBIT.write(cmd)

def report():
    msg = MBIT.read(10000)
    msg = msg.decode()
    msg_list = msg.split('\n')
    for msg in msg_list:
        print('-->', msg)

line('from microbit import display')
line('display.show(1)')
line('this is wrong ...')

sleep(1)
report()
