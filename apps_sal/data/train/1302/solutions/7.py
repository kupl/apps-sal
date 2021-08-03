# cook your dish here
from collections import defaultdict
import sys
import math
import random
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def input(): return sys.stdin.readline().strip()


for _ in range(int(input())):
    n = int(input())

    print(2 * int(math.sqrt(n // 2)))
