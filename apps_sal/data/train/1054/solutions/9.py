t = int(input())
for h in range(t):
    s = list(input())
    n = len(s)
    f = 0
    for i in range(n):
        if s[i] != '.' and s[i] != s[n - i - 1] and s[n - i - 1] != '.':
            f = 1
            print(-1)
            break
        elif s[i] == '.' and s[n - i - 1] == '.':
            s[i] = s[n - i - 1] = 'a'
        elif s[i] == '.' and s[n - i - 1] != '.':
            s[i] = s[n - i - 1]
    if f == 0:
        r = ''
        for i in s:
            r = r + i
        print(r)
