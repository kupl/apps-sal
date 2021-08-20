for i in range(int(input())):
    (n, k, e, m) = map(int, input().split())
    s = [sum(list(map(int, input().split()))) for j in range(n - 1)]
    s.sort(reverse=True)
    ob = sum(list(map(int, input().split())))
    if s[k - 1] - ob + 1 > m:
        print('Impossible')
    else:
        print(max(0, s[k - 1] - ob + 1))
