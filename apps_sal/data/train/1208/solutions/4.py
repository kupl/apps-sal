from sys import stdin, stdout
from collections import defaultdict
input = stdin.readline
print = stdout.write
T = int(input())
M = 1000000007
n = 1000005
Array = [1]
f = 1
for j in range(1, n + 1):
    Array.append(f * j * Array[j - 1] % M)
    f = f * j % M
for i in range(T):
    print(str(Array[int(input())]) + '\n')
