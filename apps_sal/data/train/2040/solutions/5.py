#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
N, H = map(int, input().split())
ret = []
for n in range(1, N):
    ret.append(H * math.sqrt(n / N))
for i in range(len(ret)):
    if i == 0:
        print("{:.15f}".format(ret[i]), end="")
    else:
        print(" {:.15f}".format(ret[i]), end="")
        

