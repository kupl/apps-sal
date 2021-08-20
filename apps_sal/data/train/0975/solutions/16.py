test = int(input())
for loop in range(test):
    flag = 0
    (sch, ele, inele) = (0, 0, 0)
    xl = []
    yl = []
    (n, r, x, y) = map(int, input().split())
    if x > 0:
        xindex = input().split()
        for q in range(x):
            xl.append(int(xindex[q]))
    if y > 0:
        yindex = input().split()
        for p in range(y):
            yl.append(int(yindex[p]))
    try:
        for a in xl:
            if a in yl:
                flag += 1
    except NameError:
        flag = 0
    sch = x + y - 2 * flag
    inele = sch + flag
    ele = n - inele
    print(min(ele, r))
