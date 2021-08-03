import sys
input = sys.stdin.readline

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

k = 10**15
s = 0
for i in range(N):
    a, b = AB[i]
    s += b
    if a > b:
        k = min(k, b)

if k == 10**15:
    print(0)
else:
    print(s - k)
