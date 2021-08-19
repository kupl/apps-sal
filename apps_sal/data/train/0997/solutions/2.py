# cook your dish here
T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    lis = [10] * N
    for z in range(M):
        i, j, k = map(int, input().split())
        for y in range(i - 1, j):
            lis[y] *= k
    tot = 0
    for i in lis:
        tot += i
    print(int(tot / N))
