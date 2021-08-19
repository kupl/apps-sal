for _ in range(int(input())):
    (M, N) = input().split()
    (m, n) = (int(M), int(N))
    x = 1 * 10 ** len(N)
    if n == x - 1:
        print(m * len(N), m)
    else:
        print(m * (len(N) - 1), m)
