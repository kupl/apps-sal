for t in range(int(input())):
    (n, q) = map(int, input().split())
    s = input()
    index = [-1] * n
    temp = -1
    for i in range(n - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 2] == s[i + 1]:
            temp = i
        index[i + 2] = temp
    for Q in range(q):
        (l, r) = map(int, input().split())
        if index[r - 1] >= l - 1:
            print('YES')
        else:
            print('NO')
