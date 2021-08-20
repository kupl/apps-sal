n = int(input())
while n > 0:
    num = 0
    t = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    sum1 = sum(a) % 3
    if sum1 == 0:
        flag = 1
    elif sum1 in a and sum1 != 0:
        c = a.index(sum1)
        del a[c]
    elif sum1 + 3 in a:
        c = a.index(sum1 + 3)
        del a[c]
    elif sum1 + 6 in a:
        c = a.index(sum1 + 6)
        del a[c]
    elif sum1 == 1:
        if 2 in a:
            c = a.index(2)
            del a[c]
            if 2 in a:
                c = a.index(2)
                del a[c]
            elif 5 in a:
                c = a.index(5)
                del a[c]
            else:
                c = a.index(8)
                del a[c]
        elif 5 in a:
            c = a.index(5)
            del a[c]
            if 5 in a:
                c = a.index(5)
                del a[c]
            elif 8 in a:
                c = a.index(8)
                del a[c]
        elif 8 in a:
            c = a.index(8)
            del a[c]
            if 8 in a:
                c = a.index(8)
                del a[c]
    elif sum1 == 2:
        if 1 in a:
            c = a.index(1)
            del a[c]
            if 1 in a:
                c = a.index(1)
                del a[c]
            elif 4 in a:
                c = a.index(4)
                del a[c]
            else:
                c = a.index(7)
                del a[c]
        elif 4 in a:
            c = a.index(4)
            del a[c]
            if 4 in a:
                c = a.index(4)
                del a[c]
            elif 7 in a:
                c = a.index(7)
                del a[c]
        elif 7 in a:
            c = a.index(7)
            del a[c]
            if 7 in a:
                c = a.index(7)
                del a[c]
    num = int(''.join(map(str, a)))
    if 0 not in a:
        num = -1
    print(num)
    n -= 1
