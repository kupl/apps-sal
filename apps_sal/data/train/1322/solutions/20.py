for T in range(int(input())):
    N, K = map(int, input().split())
    S = sorted(list(map(int, input().split())))[::-1]
    print(sum([1 for i in S if i >= S[K - 1]]))
