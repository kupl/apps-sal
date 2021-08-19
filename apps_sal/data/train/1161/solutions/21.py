for _ in range(int(input())):
    s = list(input())
    for i in range(len(s)):
        if s[i] == 'm' and i > 0 and (s[i - 1] == 's'):
            s[i - 1] = ''
        elif s[i] == 'm' and i < len(s) - 1 and (s[i + 1] == 's'):
            s[i + 1] = ''
    m = s.count('m')
    sn = s.count('s')
    if m > sn:
        print('mongooses')
    elif m < sn:
        print('snakes')
    else:
        print('tie')
