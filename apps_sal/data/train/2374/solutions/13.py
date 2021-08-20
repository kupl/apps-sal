for _ in range(int(input())):
    n = int(input())
    s = []
    s.append(input())
    s.append(input())
    k = 0
    for i in range(n):
        if s[k % 2][i] in ('1', '2'):
            continue
        if s[(k + 1) % 2][i] not in ('3', '4', '5', '6'):
            print('NO')
            break
        k += 1
    else:
        if k % 2 == 1:
            print('YES')
        else:
            print('NO')
