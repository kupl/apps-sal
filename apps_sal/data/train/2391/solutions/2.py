

def swap(i):

    tmp = a[i + 2]
    a[i + 2] = a[i + 1]
    a[i + 1] = a[i]
    a[i] = tmp
    ans.append(i + 1)


tt = int(input())

for loop in range(tt):

    n = int(input())
    a = list(map(int, input().split()))
    sa = 0.0001

    lis = [sa] * 501

    b1 = []
    b2 = []

    f2 = True
    for i in range(n):
        if lis[a[i]] != sa and f2:
            b1.append(a[i] + lis[a[i]])
            b2.append(a[i])
            f2 = False
        else:
            b1.append(a[i] + lis[a[i]])
            b2.append(a[i] + lis[a[i]])

        lis[a[i]] += sa

    ans = []
    a = b1
    for last in range(n - 3):

        mi = last
        for i in range(last, n):
            if a[i] < a[mi]:
                mi = i

        while mi != last:

            if mi - last >= 2:
                swap(mi - 2)
                mi -= 2
            else:
                swap(mi)
                mi += 1

    while not (a[-3] < a[-2] and a[-2] < a[-1]):
        swap(n - 3)

        if len(ans) > n**2:
            break

    if len(ans) <= n**2:

        print(len(ans))
        print(*ans)
        continue

    ans = []
    a = b2
    for last in range(n - 3):

        mi = last
        for i in range(last, n):
            if a[i] < a[mi]:
                mi = i

        while mi != last:

            if mi - last >= 2:
                swap(mi - 2)
                mi -= 2
            else:
                swap(mi)
                mi += 1

    while not (a[-3] < a[-2] and a[-2] < a[-1]):
        swap(n - 3)

        if len(ans) > n**2:
            break

    if len(ans) <= n**2:

        print(len(ans))
        print(*ans)
        continue

    print(-1)
