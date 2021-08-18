for _ in range(int(input())):
    s = list(input())
    n = len(s)
    for i in range(n // 2 + n % 2):
        if s[i] == '.':
            if s[n - i - 1] == '.':
                s[i], s[n - i - 1] = 'a', 'a'
            else:
                s[i] = s[n - i - 1]
        else:
            if s[n - i - 1] == '.':
                s[n - i - 1] = s[i]
            elif s[i] != s[n - i - 1]:
                print(-1)
                break
    else:
        print(''.join(s))
