for _ in range(int(input())):
    (K, N) = map(int, input().split())
    K = str(K)
    l = [int(d) for d in K]
    while N >= 5:
        print(len(set(K)) ** 3)
        break
