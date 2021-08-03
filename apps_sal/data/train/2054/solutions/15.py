from math import ceil, sqrt, factorial, gcd
from collections import deque
from sys import stdin
def input(): return stdin.readline().strip()


n = int(input())
a = []
b = []
for i in range(n - 1):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
l = list(map(int, input().split()))
ans = []
for i in range(n - 1):
    if l[a[i] - 1] != l[b[i] - 1]:
        if len(ans) == 0:
            ans = [a[i], b[i]]
        else:
            if a[i] in ans and b[i] in ans:
                print("NO")
                return
            elif a[i] in ans:
                ans = [a[i]]
            elif b[i] in ans:
                ans = [b[i]]
            else:
                print("NO")
                return
print("YES")
if ans:
    print(ans[0])
else:
    print(1)
