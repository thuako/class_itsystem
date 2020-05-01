
import numpy as np
import sys
import os
from math import *

from numpy import convolve as conv

next_flag = 1

def conv2D(a, b):
    acnum, bcnum, arnum, brnum = a.shape[0], b.shape[0], a.shape[1], b.shape[1]

    c = np.zeros((arnum+brnum-1)).reshape(1, arnum+brnum-1)
    for acolomn in a:
        for bcolomn in b:
            c = np.append(c, np.convolve(acolomn, bcolomn).reshape(1,-1), axis=0)
    c = c[1:, :]

    all = np.zeros((arnum+brnum-1)*(acnum+bcnum-1)).reshape(1, acnum+bcnum-1, -1)
    for i in range(acnum):
        tmp2 = np.zeros(i*(arnum+brnum-1)).reshape(-1,arnum+brnum-1)
        tmp1 = np.zeros((acnum - 1 - i) * (arnum + brnum - 1)).reshape(-1, arnum + brnum - 1)
        tmp3 = np.vstack((tmp1, c[bcnum*i:bcnum*(i+1), :]))
        tmp3 = np.vstack((tmp3, tmp2)).reshape(1, acnum+bcnum-1, -1)
        all = np.append(all, tmp3, axis=0)

    return all.sum(axis=0)

if len(sys.argv) >1 :
    f = open(sys.argv[1], 'r')
    parsing = []
    for a in f.readlines():
        if '[' in a:
            for i in a:
                if i.isdigit():
                    a = a.replace(i, i+',')
            if ';' in a:
                a = a.replace('[', 'np.array([[')
                a = a.replace(']', ']])')
                a = a.replace(';', '] , [')

                parsing.append(a)
            else:
                a = a.replace('[', 'np.array([')
                a = a.replace(']', '])')

                parsing.append(a)
        else:
            parsing.append(a)
    exec(''.join(parsing))


"""a = np.array([1,2])
b = np.array([1,2])

print(a.b)"""


if next_flag == 1:
    put = ''
    while put != 'quit':
        put = input(">>>")
        parsing = []
        if '[' in put:
            for i in put:
                if i.isdigit():
                    put = put.replace(i, i + ',')
            if ';' in a:
                put = put.replace('[', 'np.array([[')
                put = put.replace(']', ']])')
                put = put.replace(';', '] , [')

                parsing.append(put)
            else:
                put = put.replace('[', 'np.array([')
                put = put.replace(']', '])')

                parsing.append(put)
        elif '.*' in put:
            put = put.replace('.*', '*')
        else:
            parsing.append(put)
        exec(''.join(parsing))

