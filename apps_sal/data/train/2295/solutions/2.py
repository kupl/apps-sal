import sys
input = sys.stdin.readline
N = int(input())
s = 0
m = float('inf')
for _ in range(N):
    (A, B) = list(map(int, input().split()))
    s += A
    if A > B:
        m = min(m, B)
print(max(0, s - m))
