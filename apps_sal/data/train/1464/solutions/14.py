for i in range(int(input())):
    (y, m, d) = map(int, input().split(':'))
    if m == 1 or m == 3 or m == 5 or (m == 7) or (m == 8) or (m == 10) or (m == 12):
        s = (31 - d) // 2 + 1
    elif m == 4 or m == 6 or m == 9 or (m == 11):
        s = (61 - d) // 2 + 1
    elif y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        s = (29 - d) // 2 + 1
    else:
        s = (28 + 31 - d) // 2 + 1
    print(s)
