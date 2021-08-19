t = int(input())
for _ in range(t):
    n = int(input())
    s1 = input()
    s2 = input()
    s = [s1, s2]
    (tp1, tp2) = (['1', '2'], ['3', '4', '5', '6'])
    cur = 0
    for i in range(n):
        if s[cur][i] in tp1:
            continue
        elif s[1 - cur][i] in tp2:
            cur = 1 - cur
        else:
            print('NO')
            break
    else:
        if cur == 1:
            print('YES')
        else:
            print('NO')
