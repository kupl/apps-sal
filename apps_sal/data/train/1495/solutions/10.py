t = int(input())
for i in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    total = sum(x)
    x.sort()
    x.reverse()
    dic = {}
    (b1, b2, b0) = ([], [], [])
    for j in range(n):
        if x[j] != 0:
            if x[j] % 3 == 0:
                b0.append(x[j])
            elif x[j] % 3 == 1:
                b1.append(x[j])
            elif x[j] % 3 == 2:
                b2.append(x[j])
        if x[j] in dic:
            dic[x[j]] += 1
        else:
            dic[x[j]] = 1
    if 0 in dic:
        if total % 3 == 0:
            ans = int(''.join((str(y) for y in x)))
            print(ans)
        elif total % 3 == 1:
            flag = 1
            if len(b1) >= 1:
                x.remove(b1[-1])
            elif len(b2) >= 2:
                x.remove(b2[-1])
                x.remove(b2[-2])
            else:
                flag = 0
            if flag == 1:
                ans = int(''.join((str(y) for y in x)))
                print(ans)
            else:
                print('-1')
        elif total % 3 == 2:
            flag = 1
            if len(b2) >= 1:
                x.remove(b2[-1])
            elif len(b1) >= 2:
                x.remove(b1[-1])
                x.remove(b1[-2])
            else:
                flag = 0
            if flag == 1:
                ans = int(''.join((str(y) for y in x)))
                print(ans)
            else:
                print('-1')
    else:
        print('-1')
