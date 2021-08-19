import math
from collections import deque
from sys import stdin, stdout
from string import ascii_letters
input = stdin.readline
#print = stdout.write
letters = ascii_letters[:26]


for _ in range(int(input())):
    n = int(input())
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    nf = min(first)
    ns = min(second)
    res = 0
    for i in range(n):
        diff = first[i] - nf
        difs = second[i] - ns
        bf = min(diff, difs)
        diff -= bf
        difs -= bf
        res += bf + diff + difs
    print(res)
