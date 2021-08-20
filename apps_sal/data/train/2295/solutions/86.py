import sys
input = sys.stdin.readline
n = int(input())
A = [list(map(int, input().split())) for i in range(n)]
ans = 10 ** 10
s = 0
eq = 0
for i in range(n):
    if A[i][0] == A[i][1]:
        eq += 1
    s += A[i][0]
    if A[i][0] > A[i][1]:
        ans = min(ans, A[i][1])
if eq == n:
    print(0)
else:
    print(s - ans)
