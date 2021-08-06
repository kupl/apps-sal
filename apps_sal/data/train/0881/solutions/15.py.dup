for _ in range(int(input())):
    n = int(input())
    num = list(map(int, input().split()))
    k = [1] * n
    for i in range(n - 1):
        if num[i] <= num[i + 1]:
            k[i + 1] = k[i] + 1
    print(sum(k))
