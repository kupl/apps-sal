te = int(input())
while te > 0:
    te -= 1
    n, k = list(map(int, input().split()))
    dishes = list(input())
    heads = [0] * n
    tails = [0] * n
    for i in range(1, n):
        if dishes[i - 1] == '1':
            heads[i] = heads[i - 1] + 1
        else:
            heads[i] = 0
    j = n - 2
    while j >= 0:
        if dishes[j + 1] == '1':
            tails[j] = tails[j + 1] + 1
        else:
            tails[j] = 0
        j -= 1
    ans = 0
    i = 0
    while i + k <= n:
        ans = max(ans, heads[i] + k + tails[i + k - 1])
        i += 1
    print(ans)
