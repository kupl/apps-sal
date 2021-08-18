#!usr/bin/env python3
from collections import defaultdict
import math
def LI(): return list(map(int, input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()
def IIR(n): return [II() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]


mod = 1000000007

# A
"""
a,b = LS()
c = int(a+b)
for i in range(1,1000):
    if i * i == c:
        print("Yes")
        return
print("No")
"""

# B
"""
a,b = LI()
if a*b <= 0:
    print("Zero")
else:
    if b < 0:
        if (a-b) %2 == 1:
            print("Positive")
        else:
            print("Negative")
    else:
        print("Positive")
"""

# C
"""
n = II()
s = SR(n)
march = [[] for i in range(5)]
ch = list("MARCH")
for i in s:
    for j in range(5):
        if i[0] == ch[j]:
            march[j].append(i)
ans = 0
for i in range(5):
    for j in range(i):
        for k in range(j):
            if len(march[i])*len(march[j])*len(march[k]) == 0:
                break
            ans += len(march[i])*len(march[j])*len(march[k])
print(ans)
"""

# D
"""
n = II()
d = LIR(n)
q = II()
p = IIR(q)
d.insert(0,[0 for i in range(n+1)])
for i in range(n):
    d[i+1].insert(0,0)
for i in range(n):
    for j in range(n):
        d[i+1][j+1] += d[i+1][j]+d[i][j+1]-d[i][j]
ans = [0 for i in range(n**2+1)]

for a in range(n+1):
    for b in range(n+1):
        for c in range(a):
            for e in range(b):
                ans[(a-c)*(b-e)] = max(ans[(a-c)*(b-e)],d[a][b]-d[c][b]-d[a][e]+d[c][e])

for i in p:
    an = 0
    for a in range(i+1):
        an = max(an, ans[a])
    print(an)
"""
# E

"""
s = list(S())
ans = -1
s.insert(0,0)
d = 0
for i in range(1,len(s)):
    if s[i] != d:
        d = s[i]
        ans += 1
print(ans)
"""

# F
"""
n = II()
x,y = LI()
for _ in range(n-1):
    a,b = LI()
    if a == b:
        x = max(x,y)
        y = x
    else:
        i = max(x//a,y//b)
        while 1:
            if a*i >= x and b*i >= y:break
            i += 1
        x = a*i
        y = b*i
print(x+y)
"""
# G
"""
s = list(S())
p = 0
g = 0
for i in s:
    if i == "g":
        g += 1
    else:
        p += 1
ans = (g-p)//2
print(ans)
"""
# H
n, t = LI()
a = LI()
b = []
for i in range(n):
    b.append([i, a[i]])
b.sort(key=lambda x: x[1])
b = b[::-1]
m = []
if n == 1:
    print((1))
    return
i = 0
for j in range(n):
    while i < b[j][0]:
        m.append(b[j][1])
        i += 1
ans = 0
ma = 0
for i in range(n - 1):
    ma = max(ma, m[i] - a[i])
for i in range(n - 1):
    if m[i] - a[i] == ma:
        ans += 1
print(ans)
# I

# J

# K

# L

# M

# N

# O

# P

# Q

# R

# S

# T
