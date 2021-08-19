# cook your dish here
for i in range(int(input())):
    y, m, d = list(map(int, input().split(":")))
    if m in [1, 3, 5, 7, 8, 10, 12]:
        sol = ((31 - d) // 2) + 1
    elif m in [4, 6, 9, 11]:
        sol = ((61 - d) // 2) + 1
    else:
        if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
            sol = ((29 - d) // 2) + 1
        else:
            sol = ((59 - d) // 2) + 1
    print(sol)
