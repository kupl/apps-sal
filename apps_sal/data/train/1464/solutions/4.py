for _ in range(int(input())):
    (yy, mm, dd) = list(map(int, input().split(':')))
    if mm in [1, 3, 5, 7, 8, 10, 12]:
        sum1 = (31 - dd) // 2 + 1
    elif mm in [4, 6, 9, 11]:
        sum1 = (61 - dd) // 2 + 1
    elif yy % 4 == 0 and yy % 100 != 0 or yy % 400 == 0:
        sum1 = (29 - dd) // 2 + 1
    else:
        sum1 = (28 + 31 - dd) // 2 + 1
    print(sum1)
