for _ in range(int(input())):
    n = input().rstrip()
    n = [ele for ele in n]
    l = len(n)
    m = 10 ** 18 + 8
    ini = 1
    for i in range(l - 1, -1, -1):
        if int(n[i]) <= m:
            if ini == 1:
                m = int(n[i])
            else:
                m = max(m, n[i])
        else:
            m = int(n[i]) - 1
            n[i] = str(m)
            for j in range(l - 1, i, -1):
                n[j] = '9'
    i = 0
    while n[i] == '0':
        i += 1
    print(''.join(n[i:]))
