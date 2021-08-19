T = int(input())
for _ in range(T):
    n = int(input())
    s = list(input())
    for i in range(0, n, 2):
        s[i] = chr(122 - (ord(s[i]) - 97))
        if i % 2 == 0 and i + 1 < n:
            s[i + 1] = chr(122 - (ord(s[i + 1]) - 97))
            (s[i], s[i + 1]) = (s[i + 1], s[i])
    print(''.join(s))
