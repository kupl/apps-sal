# cook your dish here
import numpy as np


def bb(d):
    if(d == 0):
        return 0
    elif(d == 1 or d == 2):
        return 1
    else:
        return 1 + bb(d - 2**int(np.log2(d)))


T = int(input())
tests = np.zeros(T)
for i in range(T):
    tests[i] = int(input())
    print(bb(tests[i]) - 1)
