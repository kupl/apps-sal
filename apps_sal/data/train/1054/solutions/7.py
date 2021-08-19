for t in range(int(input())):
    ss = input()
    result = None
    k = ''
    s = list(ss)
    x = len(ss) - 1
    if len(ss) == 1:
        if ss == '.':
            ss = 'a'
    else:
        for i in range(len(s) // 2 + 1):
            if s[i] == s[x]:
                if s[i] == '.':
                    s[i] = 'a'
                    s[x] = 'a'
            elif s[i] == '.':
                z = s[x]
                s[i] = z
            elif s[x] == '.':
                y = s[i]
                s[x] = y
            else:
                result = -1
                break
            x = x - 1
    if result == None:
        print(k.join(s))
    else:
        print(result)
