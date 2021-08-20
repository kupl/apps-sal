import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
B = 0
C = 0
D = 0
E = 0
for i in range(n):
    a = A[i]
    if i % 2 == 0:
        B += a // 2
        C += a - a // 2
        D += a - a // 2
        E += a // 2
    else:
        B += a - a // 2
        C += a // 2
        D += a // 2
        E += a - a // 2
print(max(min(B, C), min(D, E)))
