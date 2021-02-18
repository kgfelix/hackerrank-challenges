#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    level = 0
    valleys = 0
    for s in path:
        if s == 'U':
            level += 1
        elif s == 'D':
            level -= 1
            if level == 0:
                valleys += 1


    return valleys
    


        
if __name__ == '__main__':
    ar = "DDUUDDUDUUUD"
    n = len(ar)
    result = countingValleys(n,ar)
    print(result)
