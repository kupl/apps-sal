import sys
from bisect import insort


def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return map(int, sys.stdin.readline().strip().split())


n = int(input())
Arr = []
result = []
length = 0
for i in range(n):
    t = int(input())
    insort(Arr, t)
    length += 1
    result += length - Arr.index(t),
for i in result:
    print(i)
