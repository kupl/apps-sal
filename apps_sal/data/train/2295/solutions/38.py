
import sys
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(max(1000, 10**9))
def write(x): return sys.stdout.write(x + "\n")


n = int(input())
a = [None] * n
b = [None] * n
ans = 0
same = 0
m = 0
diff = []
for i in range(n):
    a[i], b[i] = map(int, input().split())
    if a[i] < b[i]:
        ans += (b[i] - a[i])
    elif a[i] == b[i]:
        same += a[i]
    else:
        diff.append(b[i])
        m += b[i]
diff.sort()
c = 0
plus = 0
if ans == 0:
    print(0)
else:
    plus = sum(diff[1:])
    print(sum(a) - (m - plus))
