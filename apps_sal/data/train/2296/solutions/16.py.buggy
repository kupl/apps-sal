"""
どれとペアになるかは最初から確定
位置を決めれば後は転倒数
"""
import sys


def bitadd(a, w, bit):  # aにwを加える(1-origin)

    x = a
    while x <= (len(bit) - 1):
        bit[x] += w
        x += x & (-1 * x)


def bitsum(a, bit):  # ind 1～aまでの和を求める

    ret = 0
    x = a
    while x > 0:
        ret += bit[x]
        x -= x & (-1 * x)
    return ret


S = input()

dic = {}

for i, s in enumerate(S):

    if s not in dic:

        dic[s] = []

    dic[s].append(i)

pair = [None] * len(S)
lis = [None] * len(S)

for i in dic:

    for j in range(len(dic[i]) // 2):

        pair[dic[i][j]] = dic[i][-1 - j]
        pair[dic[i][-1 - j]] = -1

numnone = 0
for i in pair:
    if i == None:
        numnone += 1

if numnone > 1:
    print((-1))
    return

nmax = 0
for i, num in enumerate(pair):

    if num == None:
        lis[i] = len(S) // 2

    if num != None and num >= 0:

        lis[i] = nmax
        lis[num] = len(S) - 1 - nmax
        nmax += 1

BIT = [0] * (len(S) + 1)
ans = 0
lis.reverse()

for i, num in enumerate(lis):

    num += 1
    ans += bitsum(num, BIT)
    bitadd(num, 1, BIT)

print(ans)
