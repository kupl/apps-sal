T, = list(map(int, input().split()))
for _ in range(T):
    N, = list(map(int, input().split()))
    c = int(N**0.5)
    R = 10**18
    for i in range(max(1, c - 10), c + 10):
        R = min(R, i - (-N // i) - 2)
    print(R)
