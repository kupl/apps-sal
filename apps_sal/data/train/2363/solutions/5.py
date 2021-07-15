from collections import deque
from sys import stdin, stdout  
input = stdin.readline
#print = stdout.write

for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    print(min([arr[i + 1] - arr[i] for i in range(n - 1)]))

