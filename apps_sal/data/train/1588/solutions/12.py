for _ in range(int(input())):
    q = []
    for __ in range(int(input())):
        (a, b) = list(input().split())
        b = int(b)
        q.append((a, b))
    q = sorted(q, key=lambda x: x[1])
    i = 0
    win = ''
    if len(q) == 1:
        continue
    while i < len(q):
        t = q[i][1]
        if i == len(q) - 1 or q[i][1] != q[i + 1][1]:
            win = q[i][0]
            break
        while i < len(q) and q[i][1] == t:
            i += 1
        if i == len(q):
            break
    if win == '':
        print('Nobody wins.')
    else:
        print(win)
'\n2\n5\nKouta 1\nYuka 1\nMayu 3\nLucy 2\nNana 5\n2\nLucy 2\nNana 2\n\n'
