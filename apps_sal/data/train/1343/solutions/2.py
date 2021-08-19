# cook your dish here
import math
import numpy as np

import pandas as pd
import itertools
import collections
from collections import Counter

import copy as deepcopy


def is_double(s):
    n = len(s)
    if n % 2 == 1:
        return False
    elif n == 0:
        return False

    else:

        if s[:n // 2] != s[n // 2:n]:

            return False
        else:
            return True


try:

    T = int(input())
    for l in range(T):

        s = input()
        n = len(s)

        if is_double(s):
            print("YES")
        else:
            flag = False
            for i in range(n):
                if is_double(s[:i] + s[i + 1:]):
                    flag = True
                    break
            if flag:
                print("YES")
            else:
                print("NO")


except EOFError:
    pass
