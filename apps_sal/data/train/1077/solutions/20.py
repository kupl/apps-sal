import math
import sys


def comp(x):
    if(x == "Left"):
        return "Right"
    elif(x == "Right"):
        return "Left"
    return x


y = [""] * 45
test = int(eval(input()))
for i in range(test):
    n = int(eval(input()))
    for j in range(n):
        y[j] = input()
    prev = "Begin"
    for j in range(n):
        x = y[n - j - 1].split()
        print(comp(prev), end=' ')
        for f in x[1:]:
            print(f, end=' ')
        print()
        prev = x[0]
