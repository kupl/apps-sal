for _ in range(int(input())):
    n = input()
    a = n[::-1]
    k = 0
    for i in a:
        if i == '0':
            k += 1
        else:
            break
    print(a[k:])
