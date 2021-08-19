for _ in range(int(input())):
    s = list(input())
    start = 0
    end = len(s) - 1
    flag = True
    while start < end:
        if s[start] == '.' and s[end] != '.':
            s[start] = s[end]
        elif s[start] != '.' and s[end] == '.':
            s[end] = s[start]
        elif s[start] == '.' and s[end] == '.':
            s[start] = 'a'
            s[end] = 'a'
        elif s[start] == s[end]:
            start += 1
            end -= 1
        else:
            flag = False
            break
    if flag:
        if s[start] == '.':
            s[start] = 'a'
        print(''.join((x for x in s)))
    else:
        print(-1)
