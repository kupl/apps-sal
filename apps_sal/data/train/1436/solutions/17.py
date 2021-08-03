for i in range(int(input())):
    a = input()
    i = t = 0
    l = len(a)
    if l == 0:
        continue
    j = l - 1
    while i < l // 2:
        if a[i] != a[j]:
            t = 1
            break
        i += 1
        j -= 1
    if t == 0:
        print(1)
    else:
        print(2)
