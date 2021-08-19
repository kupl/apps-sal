for _ in range(int(input())):
    s = input()
    (a, h, t) = (list(s), 0, len(s) - 1)
    flag = 0
    while h <= t:
        if a[h] != a[t] and (a[h] != '.' and a[t] != '.'):
            flag = 1
            break
        elif a[h] == a[t] and a[h] == '.':
            a[h] = 'a'
            a[t] = a[h]
        elif a[h] != a[t]:
            if a[h] == '.':
                a[h] = a[t]
            elif a[t] == '.':
                a[t] = a[h]
        h += 1
        t -= 1
    y = ''.join(a)
    if flag == 0:
        print(y)
    else:
        print(-1)
