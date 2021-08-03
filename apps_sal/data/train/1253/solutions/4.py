t = int(input())
for i in range(t):
    n = int(input())
    s = list(input())
    d = int(input())
    p = list(map(int, input().split()))
    if s.count('1') == 0:
        print(0)
        continue
    c = 0
    e = 0
    flag = 0
    f = 0
    g = 0
    for j in range(d):
        if s[p[j] - 1] == '0':
            s[p[j] - 1] = '3'
        elif s[p[j] - 1] == '1':
            s[p[j] - 1] = '2'
        s1 = s[:]
        # print(s)
        # q1=''.join(s).lstrip('0')
        q = s[f:g + 1]
        # q=q1.rstrip('0')
        if len(q) - (c + e) == 0 and q[0] == '2' and k == g + 1:
            if c + e == 0:
                c = len(q)
            break
        c = 0
        e = 0
        for k in range(n):
            if s[k] == '1':
                if flag == 0:
                    flag = 1
                    f = k
                g = k
                c += 1
                if k == 0:
                    if s[1] == '0':
                        s1[1] = '1'
                        c += 1
                elif k == n - 1:
                    if s[k - 1] == '0':
                        s1[k - 1] = '1'
                        c += 1
                    elif s[k - 1] == '3':
                        s1[k - 1] = '2'
                        e += 1
                else:
                    if s[k + 1] == '0':
                        s1[k + 1] = '1'
                        c += 1
                    if s[k - 1] == '0':
                        s1[k - 1] = '1'
                        c += 1
                    elif s[k - 1] == '3':
                        s1[k - 1] = '2'
                        e += 1
            elif s[k] == '2':
                if flag == 0:
                    flag = 1
                    f = k
                g = k
                e += 1
                if k != n - 1:
                    if s[k + 1] == '0':
                        s1[k + 1] = '1'
                        c += 1

        s = s1[:]
        # print(s)
        # print(c,e)
    print(c + e)
