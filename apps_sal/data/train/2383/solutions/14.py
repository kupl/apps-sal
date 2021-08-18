from collections import deque
from sys import stdin, stdout
input = stdin.readline

for _ in range(int(input())):
    b, a = list(map(int, input().split()))
    print(min(max(a, b * 2), max(a * 2, b))**2)
