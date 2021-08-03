# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    f = []
    l = []
    flag = 0
    for i in a:
        if i not in d:
            f.append(i)
            d[i] = 1
        else:
            l.append(i)
            d[i] += 1
            if d[i] > 2:
                flag = 1
                break
    if flag == 1:
        print('NO')
        continue
    f.sort()
    l.sort()
    if len(l) == 0:
        print('YES')
        print(*f)
    elif f[len(f) - 1] == l[len(l) - 1]:
        print('NO')
    else:
        l.reverse()
        print('YES')
        print(*f, end=" ")
        print(*l)
