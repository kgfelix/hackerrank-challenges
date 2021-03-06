#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jump = 0
    skipNext = False
    limit = len(c) - 1

    i = 0
    while i < limit:
        if skipNext:
            skipNext = False
            i += 1
            continue
        jump += 1
        hasNextTwo = (i + 2) < len(c)
        if c[i+1] == 1 or (hasNextTwo and c[i+2] == 0):
            skipNext = True
        i += 1
        
    return jump

        
if __name__ == '__main__':
    #ar = [0, 0, 0, 0, 1, 0]
    #ar = [0, 0, 1, 0, 0, 1, 0]
    ar = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
    n = len(ar)
    result = jumpingOnClouds(ar)
    print(result)
