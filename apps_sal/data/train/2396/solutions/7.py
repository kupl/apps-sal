import math
from collections import deque
from sys import stdin, stdout
from string import ascii_letters
input = stdin.readline
#print = stdout.write
letters = ascii_letters[:26]

for _ in range(int(input())):
    n = int(input())
    nx = input().strip()
    buff = deque()
    res = 9999999
    buff.append((nx, 0, 0))
    while len(buff):
        x = buff.popleft()
        if len(x[0]) == 1:
            if x[0][0] != letters[x[1]]:
                res = min(res, x[2] + 1)
            else:
                res = min(res, x[2])
            continue
        left = x[0][:len(x[0]) // 2]
        right = x[0][len(x[0]) // 2:]
        buff.append((left, x[1] + 1, x[2] + (len(right) - right.count(letters[x[1]]))))
        buff.append((right, x[1] + 1, x[2] + (len(left) - left.count(letters[x[1]]))))
    print(res)
