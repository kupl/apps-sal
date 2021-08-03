for u in range(int(input())):
    s = list(input())
    f = 0
    n = len(s)
    i, j = 0, n - 1
    while(i <= j):
        if(s[i] == '.' and s[j] == '.'):
            s[i], s[j] = 'a', 'a'
            i += 1
            j -= 1
        elif(s[i] == '.' or s[j] == '.'):
            if(s[i] == '.' and s[j] != '.'):
                s[i] = s[j]
            else:
                s[j] = s[i]
            i += 1
            j -= 1
        elif(s[i] != '.' and s[j] != '.'):
            if(s[i] == s[j]):
                i += 1
                j -= 1
            else:
                f = 1
                break
    if(f == 1):
        print(-1)
    else:
        print(''.join(s))
