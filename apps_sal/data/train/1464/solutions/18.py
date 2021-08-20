for i in range(int(input())):
    li = input().split(':')
    y = int(li[0])
    m = int(li[1])
    d = int(li[2])
    if m == 1 or m == 3 or m == 5 or (m == 7) or (m == 8) or (m == 10) or (m == 12):
        count = (31 - d) // 2 + 1
    elif m == 4 or m == 6 or m == 9 or (m == 11):
        count = (30 + 31 - d) // 2 + 1
    elif y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        count = (29 - d) // 2 + 1
    else:
        count = (28 + 31 - d) // 2 + 1
    print(count)
