import math
T = int(input())
for i in range(T):
    (N, A, B, K) = list(map(int, input().split()))
    c = 0
    lcm = A * B // math.gcd(A, B)
    for j in range(1, N + 1):
        if j % A == 0 and j % lcm != 0:
            c += 1
        elif j % B == 0 and j % lcm != 0:
            c += 1
    if c >= K:
        print('Win')
    else:
        print('Lose')
