def dotwointervals(l1, r1, l2, r2):
    if l1 < l2 and r1 < l2:
        return 0
    elif l1 > r2 and r1 > r2:
        return 0
    return 1


n = int(input())
lofdays = []
for you in range(n):
    l = input().split()
    si = int(l[0])
    di = int(l[1])
    if you == 0:
        lofdays.append((si, si + di - 1))
        print(si, si + di - 1)
    else:
        nowint = (si, si + di - 1)
        done = 1
        for i in lofdays:
            if dotwointervals(nowint[0], nowint[1], i[0], i[1]):
                done = 0
                break
        if done == 1:
            lofdays.append(nowint)
            print(si, si + di - 1)
        else:
            mina = min(lofdays)
            if mina[0] - di > 0:
                print(1, di)
                lofdays.append((1, di))
            else:
                lofdays.sort()
                done = 0
                for i in range(1, len(lofdays)):
                    if lofdays[i][0] - lofdays[i - 1][1] - 1 >= di:
                        done = 1
                        print(lofdays[i - 1][1] + 1, lofdays[i - 1][1] + di)
                        lofdays.append((lofdays[i - 1][1] + 1, lofdays[i - 1][1] + di))
                        break
                if done == 0:
                    print(lofdays[-1][1] + 1, lofdays[-1][1] + di)
                    lofdays.append((lofdays[-1][1] + 1, lofdays[-1][1] + di))
