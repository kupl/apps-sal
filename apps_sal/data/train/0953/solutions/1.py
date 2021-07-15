import random

def solve(n):
    b = 2*n + 3
    num = b - pow( b**2 - 4*n*(n+1), 0.5)
    ans = int(num // 2)
    return ans


for case in range(int(input())):
    n = int(input())
    print(solve(n))

