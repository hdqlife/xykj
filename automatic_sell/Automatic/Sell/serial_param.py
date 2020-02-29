import serial #导入模块
import threading
STRGLO="" #读取的数据
BOOL=True  #读取标志位
from .crc16 import *
from .views import *

#读数代码本体实现
def ReadData(ser):
    global STRGLO,BOOL

    while BOOL:
        if ser.in_waiting:
            STRGLO = ser.read(ser.in_waiting).decode("gbk")
            print(STRGLO)

#打开串口
def DOpenPort(port,baudrate,bytesize,parity,stopbits):
    ser=None
    ret=False
    try:

        ser = serial.Serial(port, baudrate, bytesize, parity, stopbits)
        if(ser.is_open):
           ret=True
           threading.Thread(target=ReadData, args=(ser,)).start()
    except Exception as e:
        print("异常：", e)
    return ser,ret

#关闭串口
def DColsePort(ser):
    global BOOL
    BOOL=False
    ser.close()

#写数据
def DWritePort(ser,text):
    result = ser.write(text.encode("utf-8"))
    return result

#读数据
def DReadPort():
    global STRGLO
    str=STRGLO
    STRGLO=""#清空当次数据
    return str

def test():
    ser = None
    ret=DOpenPort("COM3",38400,8,"N",1)
    # input_read = input("发送命令：")
    # reads = crc16.crc16Check(input_read)
    print(ser)
    print(ret)
    if(ret==True):#判断端口是否成功打开
        # from PyQt5 import QtCore, QtGui, QtWidgets
        while True:
            read = input("发送命令：")
            reads=crc16Check(read)
            # print('Modbus-CRC-16校验：', reads)
            hex_str=bytes.fromhex(reads)
            n=ser.write(hex_str)
            # n=ser.inwaiting()
            if n:
                data=str(binascii.b2a_hex(ser.read(n)))[2:-1]
                print(data)

            time.sleep(1)
import binascii
import time
if __name__=="__main__":
    test()
            # print(type(read))



