x = int(input())
for i in range(0, x):
    y = int(input())
    list = []
    for p in range(0, y):
        m = input()
        list.append(m)
    listans = []
    s = list[y - 1]
    s = s.split(' ')
    s[0] = 'Begin'
    q = ''
    flag = 0
    for r in s:
        if flag == 1:
            q = q + ' '
        else:
            flag = 1
        q = q + r
    listans.append(q)
    listk = []
    for p in range(0, y - 1):
        q = ''
        flag = 0
        s = list[p]
        r = list[p + 1]
        r = r.split(' ')
        s = s.split(' ')
        if r[0] == 'Right':
            s[0] = 'Left'
        else:
            s[0] = 'Right'
        for r in s:
            if flag == 1:
                q = q + ' '
            else:
                flag = 1
            q = q + r
        listk.append(q)
    for z in range(0, len(listk)):
        listans.append(listk[len(listk) - 1 - z])
    for z in listans:
        print(z)
