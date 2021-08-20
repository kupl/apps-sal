for i in range(int(input())):
    n = int(input())
    s1 = input()
    s2 = input()
    a = [s1, s2]
    lvl = 0
    f = True
    for i in range(n):
        if '1' <= a[lvl][i] <= '2':
            continue
        elif '1' <= a[(lvl + 1) % 2][i] <= '2':
            f = False
            break
        else:
            lvl = (lvl + 1) % 2
    print('YES' if f and lvl == 1 else 'NO')
