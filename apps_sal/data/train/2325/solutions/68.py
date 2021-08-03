# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

#n,m = map(int,readline().split())
s = input()
t = input()

vs = [0]
for i in s:
    if i == "A":
        vs.append(vs[-1] + 1)
    else:
        vs.append(vs[-1] - 1)

vt = [0]
for i in t:
    if i == "A":
        vt.append(vt[-1] + 1)
    else:
        vt.append(vt[-1] - 1)

# print(vs)
# print(vt)

q = int(input())
for _ in range(q):
    a, b, c, d = list(map(int, readline().split()))
    rs = vs[b] - vs[a - 1]
    rs %= 3

    rt = vt[d] - vt[c - 1]
    rt %= 3

    if rs == rt:
        print("YES")
    else:
        print("NO")
