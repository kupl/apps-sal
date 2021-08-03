for t in range(int(input())):
    x, y, n = map(int, input().split())
    n += 1
    count = 0
    flag = 0
    for i in range(29, -1, -1):
        if flag == 0:
            if(x & (1 << i)) != (y & (1 << i)):
                for k in range(29, -1, -1):
                    if (n & (1 << k)):
                        if k > i:
                            count += (1 << (k - 1))
                        elif k == i:
                            if (x & (1 << i)) == 0:
                                count += (1 << k)
                        else:
                            if (x & (1 << i)) == (n & (1 << i)):
                                count += (1 << k)
                flag = 1
    print(count)
