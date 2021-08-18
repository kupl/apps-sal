try:
    T = int(input())
    ans = []
    for _ in range(T):
        n = int(input())
        a = [0] * n
        for i in range(0, n, 2):
            a[i] = i + 2
            if i == n - 1:
                a[i] = a[i - 1]
                a[i - 1] = i + 1
            else:
                a[i + 1] = i + 1

        ans.append(a)
    for _ in range(T):
        print(' '.join(map(str, ans[_])))
except EOFError:
    pass
