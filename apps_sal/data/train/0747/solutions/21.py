t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = []
    c = []
    flag = 0
    i = 0
    if a.count(a[-1]) > 1:
        flag = 1

    while i < n:
        if a.count(a[i]) > 2:
            flag = 1
            break
        elif a.count(a[i]) == 2 and flag != 1:
            b.append(a[i])
            c.append(a[i])
            i += 1
        else:
            b.append(a[i])
        i += 1
    c = c[::-1]
    if flag == 1:
        print("NO")
    else:
        print("YES")
        print(*(b + c))

    t -= 1
