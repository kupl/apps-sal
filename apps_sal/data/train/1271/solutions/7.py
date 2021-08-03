t = int(input())
for i in range(t):
    n = int(input())
    a = []
    s = set()
    cta, ctb = 0, 0
    while(n != 0):
        x = int(input())
        m = len(a)
        if(x not in s):
            s.add(x)
            a.append(x)
            s2 = bin(x).count('1')
            if(s2 % 2 == 0):
                cta += 1
            else:
                ctb += 1
            for i in range(m):
                y = x ^ a[i]
                # print(y)
                if(y not in s):
                    s.add(y)
                    a.append(y)
                    s2 = bin(y).count('1')
                    if(s2 % 2 == 0):
                        cta += 1
                    else:
                        ctb += 1
        print(cta, ctb)
        n -= 1
