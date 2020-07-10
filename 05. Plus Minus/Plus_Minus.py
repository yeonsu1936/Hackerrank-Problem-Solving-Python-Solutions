#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = list()
    neg = list()
    zero = list()
    for i in arr:
        if i > 0:
            pos.append(i)
        elif i == 0:
            zero.append(i)
        elif i < 0:
            neg.append(i)
    pos_rate = len(pos)/n
    neg_rate = len(neg)/n
    zero_rate = len(zero)/n
    print('%.6f'%pos_rate)
    print('%.6f'%neg_rate)
    print('%.6f'%zero_rate)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)