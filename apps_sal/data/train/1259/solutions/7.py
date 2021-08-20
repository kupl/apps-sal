for _ in range(int(input())):
    (l, r) = map(int, input().split())
    c = 0
    while l <= r:
        i = 1
        if str(l)[-1] == '2':
            c += 1
            i = 1
        elif str(l)[-1] == '3':
            c += 1
            i = 6
        elif str(l)[-1] == '9':
            c += 1
            i = 3
        l += i
    print(c)
