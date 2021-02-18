#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    socks = {}
    total = 0
    for s in ar:
        if s in socks:
            socks[s] = socks[s] + 1
            if (socks[s]  % 2) == 0:
                total = total + 1
        else:
            socks[s] = 1

    return total


if __name__ == '__main__':
    ar = [1,2,1,2,1,3,2]
    n = len(ar)
    result = sockMerchant(n, ar)
    print(result)
