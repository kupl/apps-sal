T = int(input())
for _ in range(T):
    s = input()
    if len(s) > 3:
        g = s[::-1]
        if g[0:4] == '0001':
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
