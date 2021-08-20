for _ in range(int(input())):
    n = int(input())
    s = input()
    r = input()
    c = 0
    c1 = 0
    for j in s:
        if j == '1':
            c += 1
    for k in r:
        if k == '1':
            c1 += 1
    if c == c1:
        print('YES')
    else:
        print('NO')
