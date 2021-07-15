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


class StockSpanner:

    def __init__(self):
        self.s = []
        self.i = 0

    def next(self, price: int) -> int:
        s = self.s
        i = self.i

        while len(s) and s[-1][0] <= price:
            s.pop()

        ans = i + 1
        if len(s):
            ans = i - s[-1][1]
        s.append((price, i))
        self.i += 1
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
\"\"\"
s = StockSpanner()

print(s.next(100))
print(s.next(80))
print(s.next(60))
print(s.next(70))
print(s.next(60))
print(s.next(75))
print(s.next(85))
\"\"\"

