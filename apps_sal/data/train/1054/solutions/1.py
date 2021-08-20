for _ in range(int(input())):
    s = list(input())
    n = len(s)
    f = 0
    for i in range(n // 2):
        if s[i] == '.' and s[n - i - 1] == '.':
            s[i] = 'a'
            s[n - i - 1] = 'a'
        elif s[i] == '.':
            s[i] = s[n - i - 1]
        elif s[n - i - 1] == '.':
            s[n - i - 1] = s[i]
        elif s[i] != s[n - i - 1]:
            f = 1
            break
        else:
            continue
    if f:
        print('-1')
    else:
        if n % 2:
            if s[n // 2] == '.':
                s[n // 2] = 'a'
        print(''.join(s))
