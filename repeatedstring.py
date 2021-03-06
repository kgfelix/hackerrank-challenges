#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.

def repeatedString(s, n):
    s_list = list(s)
    str_len = len(s_list)
    total_occur = 0

    if n >= str_len:
        total_occur = s_list.count("a")
        n_repeats = n // str_len
        if n_repeats > 0:
            total_occur = total_occur * n_repeats
            remaining = n - (n_repeats * str_len)
            if remaining > 0:
                total_remaining = s_list[0:remaining].count("a")
                total_occur += total_remaining
    else:
        total_occur = s_list[0:n].count("a")    

    return total_occur

if __name__ == '__main__':
    s = "aba"
    n = 10
    #s = "a"
    #n = 1000000000000000000000000000000000000000
    result = repeatedString(s,n)
    print(result)
