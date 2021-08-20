import math
T = int(input())
for _ in range(T):
    (N, A, K) = list(map(int, input().split(' ')))
    total = (N - 2) * 180
    diffT = total - N * A
    diffN = sum(range(1, N))
    r = A * diffN + (K - 1) * diffT
    d = math.gcd(r, diffN)
    while d > 1:
        r //= d
        diffN //= d
        d = math.gcd(r, diffN)
    print(r, diffN)
