#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time = 0
    if 'PM' in (s):
        time = abs(int(s[0:2])+12)
        if(s[0:2] == '12'):
            time = 12
        s = s.replace(s[0:2], str(time))
        return(s[0:-2].zfill(8))
    else:
        if(int(s[0:2])<12):
            time = int(s[0:2])
        if(s[0:2] == '12'):
            time = str(00)
        s = s.replace(s[0:2], str(time))
        return(s[0:-2].zfill(8))

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()