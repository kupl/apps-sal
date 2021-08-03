for T in range(int(input())):
    N, P = map(int, input().split())
    M = count = 0
    for i in range(1, P + 1):
        for j in range(1, P + 1):
            for k in range(1, P + 1):
                m = N % i % j % k % N
                if M < m:
                    count = 1
                    M = m
                elif M == m:
                    count += 1
    print(count)
