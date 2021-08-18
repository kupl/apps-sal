try:
    for _ in range(int(input())):
        n, k = map(int, input().split())
        ans = [0] * n
        for i in range(k):
            ans[i] = i + 1
        ans[k] = n
        ans[n - 1] = k + 1
        for j in range(k + 1, n - 1):
            ans[j] = j + 1
        print(*ans)

except:
    pass
