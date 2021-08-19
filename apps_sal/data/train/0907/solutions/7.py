for _ in range(int(input())):
    n = int(input())
    s = input()
    (h, t, prev, flag) = (0, 0, '', 0)
    for i in s:
        if prev == '' and i == 'T':
            flag = 1
        if i == 'H':
            h += 1
            if prev == 'H':
                flag = 1
        elif i == 'T':
            t += 1
            if prev == 'T':
                flag = 1
        if i in ('H', 'T'):
            prev = i
    print('Invalid' if flag == 1 else 'Invalid' if h != t else 'Valid')
