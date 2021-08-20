import sys
input = sys.stdin.readline
'\na,b=[],[]\nfor i in range():\n    A, B = map(int, input().split())\n    a.append(A)   \n    b.append(B)'
n = int(input())
a = list(map(int, input().split()))
x = 0
for item in a:
    x ^= item
ans = []
for item in a:
    ans.append(x ^ item)
ans = map(str, ans)
print(' '.join(ans))
