# a
"""
import math
a, b = map(str, input().split())
j = int(a + b)
if math.sqrt(j).is_integer():
    print("Yes")
else:
    print("No")
"""

# b
"""
ans = ["Positive","Negative"]
a, b = map(int, input().split())
if 0 < a:
    print("Positive")
elif b >= 0:
    print("Zero")
else:
    print(ans[(b-a)%2-1])
"""

# C
"""
import itertools
n = int(input())
MARCH = ["M", "A", "R", "C", "H"]
march = [0 for _ in range(5)]
for i in range(n):
    s = input()
    if s[0] in MARCH:
        march[MARCH.index(s[0])] += 1
num = list(range(5))
a = list(itertools.combinations(num, 3))
ans = 0
for i in a:
    bf = 1
    for k in i:
        bf *= march[k]
    ans += bf
print(ans)
"""

# D
"""
n = int(input())
D = [list(map(int, input().split())) for _ in range(n)]
q = int(input())
p = [int(input()) for _ in range(q)]
ans = [[0 for i in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        break
for _ in p:
    print(ans[p])
"""

# E
"""
s = input()
bf = s[0]
ans = 0
for i in range(1,len(s)):
    if bf != s[i]:
        ans += 1
        bf = s[i]
print(ans)
"""

# F
"""
n = int(input())
ta = [list(map(int, input().split())) for _ in range(n)]
ans = ta[0]
for i in ta:
    if ans[0] <= i[0] and ans[1] <= i[1]:
        ans = i
    else:
        a = ((ans[0] - 1) // i[0]) + 1
        b = ((ans[1] - 1) // i[1]) + 1
        ab = max(a,b)
        ans = [i[0] * ab, i[1] * ab]
print(ans[0]+ans[1])
"""

# G
n, t = map(int, input().split())
a = list(map(int, input().split()))
minv = a[0]
maxv = 0
ans = 0
for i in range(1, n):
    if maxv == a[i] - minv:
        ans += 1
    elif maxv < a[i] - minv:
        maxv = a[i] - minv
        ans = 1
    else:
        minv = min(minv, a[i])
print(ans)

# H
"""
s = input()
ans = 0
for i in range(1,len(s)):
    if i % 2 == 1:
        if s[i] != "p":
            ans += 1
    else:
        if s[i] != "g":
            ans -= 1
print(ans)
"""
