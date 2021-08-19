for _ in range(int(input())):
    s = str(input())
    n = len(s)
    k = s[::-1]
    (a, b) = ('', '')
    for i in range(n):
        if s[i] != k[i]:
            a += s[i + 1:]
            b += k[i + 1:]
            break
        else:
            a += s[i]
            b += k[i]
    if a == a[::-1] or b == b[::-1]:
        print('YES')
    else:
        print('NO')
