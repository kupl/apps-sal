for t in range(int(input())):
    (n, m) = list(map(int, input().split()))
    x = [10] * n
    for i in range(m):
        (i, j, k) = list(map(int, input().split()))
        for j in range(i - 1, j):
            x[j] *= k
    print(int(sum(x) / n))
