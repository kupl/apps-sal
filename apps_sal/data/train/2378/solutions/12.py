from math import *
import os
import sys
from io import BytesIO

for i in range(int(input())):
    s = input()
    d = {}
    d["L"] = 0
    d["R"] = 0
    d["U"] = 0
    d["D"] = 0
    for c in s:
        d[c] += 1
    if d["U"] == 0 or d["D"] == 0:
        d["U"] = 0
        d["D"] = 0
    if d["R"] == 0 or d["L"] == 0:
        d["R"] = 0
        d["L"] = 0

    if d["R"] == 0 or d["L"] == 0:
        if d["U"] != 0 and d["D"] != 0:
            print(2)
            print("UD")
            continue
        else:
            print(0)
            continue
    if d["U"] == 0 or d["D"] == 0:
        if d["L"] != 0 and d["R"] != 0:
            print(2)
            print("LR")
            continue
        else:
            print(0)
            continue
    else:
        x = min(d["U"], d["D"])
        y = min(d["L"], d["R"])
        print(2 * x + 2 * y)
        print("U" * x + "L" * y + "D" * x + "R" * y)
