t = eval(input())
MOD = 1000000007
temp = [0]*1025
for xx in range(0,t):
    inp = input()
    n = eval(input())
    ct = [0]*1025
    ans = [0]*1025
    while(n):
        s = input()
        m = 0
        j = 9
        c = 1
        while(j >= 0):
            if(s[j]=='+'):
                m |= c
            c <<= 1
            j -= 1
        ct[m] += 1
        n -= 1

    for i in range(0,1024):
        m = i
        c = ct[i]
        while(c):
            for j in range(0,1024):
                temp[j] = ans[m^j]
            temp[m] += 1
            for j in range(0,1024):
                ans[j] += temp[j]
                if(ans[j] > 100000000000000000):
                    ans[j] %= MOD
            c -= 1
    
    ans[0] += 1
    s = []
    for i in range(0,10):
        if(inp[i] == 'b'):
            s.append('-')
        else:
            s.append('+')
    m = 0
    j = 9
    c = 1
    while(j >= 0):
        if(s[j]=='+'):
            m |= c
        c <<= 1
        j -= 1
    print(ans[m]%MOD)

