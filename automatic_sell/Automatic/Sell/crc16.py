from binascii import *
from crcmod import *
import serial
import sys

# ser = serial.Serial(port='COM2',
#                     baudrate=38400,
#                     parity=serial.PARITY_ODD,
#                     stopbits=serial.STOPBITS_TWO,
#                     bytesize=serial.SEVENBITS
# )

def crc16Check(read):
    crc16 = crcmod.mkCrcFun(0x18005, rev=True, initCrc=0xFFFF, xorOut=0x0000)
    data = read.replace(" ", "")
    # print(type(unhexlify(data)))
    # print(type(crc16(unhexlify(data))))
    # print(type(data))
    # readcrcout = hex(crc16(unhexlify(data)))
    # print(type(readcrcout))
    readcrcout = hex(crc16(unhexlify(data))).upper()
    # print(readcrcout)
    str_list = list(readcrcout)
    # print(str_list)
    if len(str_list) == 5:
        str_list.insert(2, '0')
        print(str_list)
    crc_data = "".join(str_list)
    # print(crc_data)
    read = read.strip() + ' ' + crc_data[4:] + ' ' + crc_data[2:4]
    print(read)
    print('CRC-16校验:', crc_data[4:] + ' ' + crc_data[2:4])
    return read


# if __name__ == '__main__':
#
#         while True:
#             read=input("发送命令：")
#             crc16Check(read)
