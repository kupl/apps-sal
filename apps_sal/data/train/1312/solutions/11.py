t = eval(input())
for ti in range(t):
    x = [int(i) for i in input().split()]
    found = False
    a = []
    for i in range(x[0]):
        a.append(input().lower())
    for i in range(x[0]):
        if a[i].find("spoon") != -1:
            found = True
            break
    if not found:
        for j in range(x[1]):
            str = ""
            for i in range(x[0]):
                str += a[i][j]
            if str.find("spoon") != -1:
                found = True
                break
    if found:
        print("There is a spoon!")
    else:
        print("There is indeed no spoon!")
