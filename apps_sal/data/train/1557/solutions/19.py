t = int(input())
for i in range(t):
    l = int(input())
    s = input()
    r = input()
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    for i in range(l):
        if s[i] == '0':
            c1 += 1
        else:
            c2 += 1
    for j in range(l):
        if r[j] == '0':
            c3 += 1
        else:
            c4 += 1
    if c1 == c3 and c2 == c4:
        print('YES')
    else:
        print('NO')
