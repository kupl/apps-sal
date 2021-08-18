def fun(s):
    p = 0
    m = 0
    for i in range(n - 1):
        if s[i] == '1' and s[i + 1] == '1':
            p += 1
        else:
            p = 0
        m = max(m, p)
    return m + 1


for __ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    r = 0
    for i in range(n - k + 1):
        s1 = '1' * k
        h = fun(s[:i] + s1 + s[i + k:])
        r = max(r, h)
    print(r)
