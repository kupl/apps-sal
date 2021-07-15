from math import floor
from math import ceil
from math import sqrt
from collections import deque
import numpy
from _collections import deque
#from _ast import Num # LC doesn't like this
from heapq import *
from typing import List
import random

MOD = int(1e9 + 7)
BASE = 256


class ProductOfNumbers:

    def __init__(self):
        self.p = [1]
        self.last0i = -1

    def add(self, num: int) -> None:
        p = self.p
        N = len(p)
        if num == 0:
            self.last0i = N
            num = 1
        p.append(p[-1] * num)

    def getProduct(self, k: int) -> int:
        p = self.p
        si = len(p) - k
        if si <= self.last0i:
            return 0
        else:
            return p[-1] // p[si - 1]

\"\"\"
s = ProductOfNumbers()
s.add(3)
s.add(0)
s.add(2)
s.add(5)
s.add(4)
print(s.getProduct(2))
print(s.getProduct(3))
print(s.getProduct(4))
s.add(8)
print(s.getProduct(2))
\"\"\"
