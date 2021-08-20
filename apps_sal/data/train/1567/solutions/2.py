try:
    t = int(input())
    for i in range(t):
        n = int(input())
        s = input()
        flag = 1
        d = dict()
        for j in range(n):
            d[s[j]] = 0
        for j in range(n):
            d[s[j]] = d[s[j]] + 1
        flag = 1
        if n // 2 % 2 == 0:
            for j in list(d.keys()):
                if d[j] % 2 != 0:
                    flag = 0
                    break
            if flag == 1:
                print('YES')
            else:
                print('NO')
        else:
            count = 0
            for j in list(d.keys()):
                if d[j] % 2 != 0:
                    count = count + 1
            if count == 2 or count == 0:
                print('YES')
            else:
                print('NO')
except:
    pass
