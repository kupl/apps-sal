for i in range(eval(input())):
    n = eval(input())
    a = []
    ans = 0
    b = list(map(int, input().split()))
    for j in range(1, n + 1):
        temp = b[j - 1]
        if temp == 0:
            a.insert(0, j)
        else:
            k = 0
            while a[k] != temp:
                k += 1
            a.insert(k + 1, j)
            ans += min(k + 1, j - k - 2)
    print(ans)
