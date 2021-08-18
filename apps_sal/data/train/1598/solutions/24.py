"""
Created on Thu Jul 30 11:31:06 2020

@author: MONIMOY
"""

t = int(input())


def sortkey(ele):
    return int(ele[2])


def avg(s):
    total = 0
    for i in range(len(s)):
        total += int(s[i][2])
    return total / len(s)


out = []
for i in range(t):
    n = int(input())
    s = []

    for j in range(n):
        a = input().split()
        s.append(a)
    s.sort(key=sortkey)
    av = avg(s)
    for k in s:
        if int(k[2]) < av:
            out.append(k)

for i in range(len(out)):
    print(*out[i], sep=" ")
