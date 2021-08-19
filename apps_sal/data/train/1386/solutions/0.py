from math import factorial
for _ in range(int(input())):
    (N, M) = [int(a) for a in input().split()]
    print(float(N + M - 1))
