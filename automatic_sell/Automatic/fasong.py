# import serial
# import binascii
#
# ser = serial.Serial()
#
#
# def port_open():
#     ser.port = "COM3"  # 设置端口号
#     ser.baudrate = 38400  # 设置波特率
#     ser.bytesize = 8  # 设置数据位
#     ser.stopbits = 1  # 设置停止位
#     ser.parity = "N"  # 设置校验位
#     ser.open()  # 打开串口,要找到对的串口号才会成功
#     if (ser.isOpen()):
#         print("打开成功")
#     else:
#         print("打开失败")
#
#
# def port_close():
#     ser.close()
#     if (ser.isOpen()):
#         print("关闭失败")
#     else:
#         print("关闭成功")
#
#
# def send(send_data):
#     if (ser.isOpen()):
#         # ser.write(send_data.encode('utf-8'))  # utf-8 编码发送
#         ser.write(binascii.a2b_hex(send_data))  #Hex发送
#         print("发送成功", send_data)
#     else:
#         print("发送失败")
#
#
# if __name__ == "__main__":
#     port_open()
#     # port_close()
#     # while True:
#     send("01 02 00 01 00 01 ")


import serial
import time  # 延时使用
import binascii

s = serial.Serial("COM3",baudrate=38400, bytesize=8, parity='N', stopbits=1, timeout=2)  # 初始化串口
s.open()
while True:

    Hex_str = bytes.fromhex('01 03 00 01 00 01 D5 CA')  # 文本转换Hex
    # =bytes.fromhex('10 11 12 34 3f')
    s.write(Hex_str)  # 串口发送 Hex_str()
    # 接收
    n = s.inWaiting()  # 串口接收
    if n:
        data = str(binascii.b2a_hex(s.read(n)))[2:-1]  # Hex转换成字符串
        print(data)  # 字符串输出
    time.sleep(1)

