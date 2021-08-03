for _ in range(eval(input())):
    a = list(map(int, input().split()))
    s = [a[1], a[2]]
    e = [a[3], a[4]]
    b = [a[5], a[6]]
    c = abs(e[1] - s[1]) + abs(e[0] - s[0])
    if b[0] == e[0] and b[1] < e[1]:
        c += 2
        print(c)
    else:
        print(c)
