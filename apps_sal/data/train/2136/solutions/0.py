import sys
readline = sys.stdin.readline
N = int(readline())
A = list(map(int, readline().split()))
BW = [0, 0]
for i in range(N):
    a = A[i]
    BW[i % 2] += a // 2
    BW[(i + 1) % 2] += -(-a // 2)
print(min(BW))
