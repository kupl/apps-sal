for _ in range(int(input())):
    a = input()
    count = 0
    if a[0] == '0':
        print(count)
    else:
        s = 0
        for i in a:
            if i == '0':
                count += 1
                s += 1
            elif s > 0:
                break
        print(count)
