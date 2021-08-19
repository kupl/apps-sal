for t in range(int(input())):
    (n, k) = list(map(int, input().split()))
    s = input()
    i = 0
    j = 0
    ans = 0
    while i < n and j < n:
        if s[i] == 'M':
            if s[j] == 'I':
                c = 0
                if i > j:
                    o = s[j:i]
                    c = o.count(':')
                else:
                    o = s[i:j]
                    c = o.count(':')
                p = k + 1 - abs(i - j) - c
                if p > 0:
                    ans = ans + 1
                    i = i + 1
                    j = j + 1
                elif i < j:
                    i += 1
                else:
                    j += 1
            elif s[j] == 'X':
                j += 1
                i = j
            else:
                j += 1
        elif s[i] == 'X':
            i += 1
            j = i
        else:
            i += 1
    print(ans)
