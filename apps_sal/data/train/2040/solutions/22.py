# -*- coding: utf-8 -*-

import sys
import os
import math

# input_text_path = __file__.replace('.py', '.txt')
# fd = os.open(input_text_path, os.O_RDONLY)
# os.dup2(fd, sys.stdin.fileno())

n, h = map(int, input().split())

X = []
for i in range(1, n):
    c = math.sqrt(i / n) * h
    X.append(c)

print(*X)
