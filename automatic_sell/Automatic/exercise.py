import pandas as pd
import numpy as np
from mxnet import nd
import struct

# address=[0,1,2,3,4,5]
# for addr in address:
#     put_addr="%02d"% addr
#     order=[3,5]
#     for ord in order:
#         put_ord="%02d"% ord
#         # print(put_ord)
#         goods_1=[0,1,2,3,4,5,6,7]
#         goods_2=[0,1,2,3,4,5,6,7,8,9]
#         for go_1 in goods_1:
#             put_good_1="%02d"% go_1
#             # print(put_good_1)
#
#             for go_2 in goods_2:
#                 put_good_2="%02d"% go_2
#                 # print(put_good_2)
#                 goods=put_good_1+put_good_2
#                 # print(goods)
#
#
#                 shopput_order = ["FF00", "00FF"]
#                 if len(shopput_order)==2:
#                     for shopput in shopput_order:
#                         # print(shopput)
#                         if put_ord =="05":
#                             shopput_order=shopput
#                             by_join = put_addr + put_ord + goods + shopput_order
#                             s=str(by_join).split(" ")
#                             # my=r"\x"
#                             fin=""
#                             for i in range(len(s)):
#                                 fin =  fin + '{:02X}'.format(s[i]) + ' '
#                             print(fin)
#                             print(by_join)
                # elif shopput_order == "0001":
                #     for shopput in shopput_order:
                #
                #         by_join=put_addr+put_ord+goods+shopput_order
                #         print(by_join)


# def pipei(str1):
#     a = str1[0:2]
#     b = str1[2:4]
#     c = str1[4:8]
#     d = str1[8:12]
#     a_list = []
#     for i in range(0,6):
#         a1 = '0' + f'{i}'
#         a_list.append(a1)
#     b_list = ['03','05']
#     c_list = []
#     for j in range(0,710):
#         c1 = '0'+ f"{'%03d'%j}"
#         c_list.append(c1)
#     for ax in a_list:
#         if ax == a:
#             for bx in b_list:
#                 if bx == b:
#                     if (b == '03' and d == '0001') or (b == '05' and d == 'FF00') or (b == '05' and d == '00FF'):
#                         for cx in c_list:
#                             if cx == c:
#                                 print("匹配成功")


# def pipei(str1):
#     a = str1[0:2]
#     b = str1[2:4]
#     c = str1[4:8]
#     d = str1[8:12]
#     s = [0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF]
#     a_list = []
#     for i in range(0x0,0x6):
#         a1 = '0' + f'{i}'
#         a_list.append(a1)
#     b_list = [0x03,0x05]
#     c_list = []
#     for j in range(0x0,0x80):
#         c1 = 0x0+ f"{'%03d'%j}"
#         c_list.append(c1)
#     for w in range(0x0,0x7):
#         for n in s:
#             for m in s:
#                 c2 = '0'+str(w)+n + m
#                 c_list.append(c2)
#     for ax in a_list:
#         if ax == a:
#             for bx in b_list:
#                 if bx == b:
#                     if (b == 0x03 and d == 0x0001) or (b == 0x05 and d == 0xFF00) or (b == 0x05 and d == 0x00FF):
#                         for cx in c_list:
#                             if cx == c:
#                                 print("匹配成功")
#                                 break
#                         else:
#                             print("不成功")
#                     break
#             else:
#                 print("不成功")
#             break
#     else:
#         print("不成功")

