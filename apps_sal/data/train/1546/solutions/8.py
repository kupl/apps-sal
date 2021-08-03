for test_case in range(int(input())):
    l = sorted(list(map(int, input().split())))
    # print(l)

    x = l[0]**2
    y = l[1]**2
    z = l[2]**2

    # print(x, y, z)
    if x != 0 and y != 0 and z != 0:
        if x + y == z:
            print("YES")
        else:
            print("NO")

    else:
        print("NO")
