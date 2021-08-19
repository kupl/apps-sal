for _ in range(int(input())):
    (N, Q) = list(map(int, input().split()))
    z = (N + Q + 1) * Q / (Q + 1)
    print(z)
