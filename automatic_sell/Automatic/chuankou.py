# coding:utf-8

import serial.tools.list_ports

plist = list(serial.tools.list_ports.comports())

if len(plist) <= 0:
    print("没有端口")
else:
    plist_0 = list(plist[0])
    serialName = plist_0[0]
    serialFd = serial.Serial(serialName, 38400, 8,"N",1,timeout=2)
    print("可用端口:", serialFd.name)
cmd = [0x01, 0x05, 0x91, 0xF5, 0x00, 0x00, 0xF1, 0x04]

import serial
class Ser(object):
    def __init__(self):
        # 打开端口
        self.port = serial.Serial(port='COM3', baudrate=38400, bytesize=8, parity='N', stopbits=1, timeout=2)

    # 发送指令的完整流程
    def send_cmd(self, cmd):

        self.port.write(cmd)
        response = self.port.readall()
        response = self.convert_hex(response)

        return response

    # 转成16进制的函数
    def convert_hex(self, string):
        res = []
        result = []
        for item in string:
            res.append(item)
        for i in res:
            result.append(hex(i))
        return result
a=Ser
