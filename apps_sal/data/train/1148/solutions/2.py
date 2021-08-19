def is_better(x, y):
    # print("x y", x, y)
    for i in range(3):
        if s[y][i] > s[x][i]:
            # print("sd", i, s[y][i], s[x][i])
            return 0

    for i in range(3):
        if s[x][i] > s[y][i]:
            # print("sank")
            return 1

    # print("mon")
    return 0


t = int(input())

for _ in range(t):
    # print("t", _)
    s = []

    for i in range(3):
        s.append([int(x) for x in input().split()])

    # print(s)

    f = -1
    m = -1

    flag = 1

    # if(f == -1):
    if(is_better(0, 1) and is_better(0, 2)):
        f = 0
    elif(is_better(1, 0) and is_better(1, 2)):
        f = 1
    elif(is_better(2, 0) and is_better(2, 1)):
        f = 2
    else:
        flag = 0

    if(f != -1):
        temp = [0, 1, 2]
        temp.remove(f)

        if(is_better(temp[0], temp[1])):
            m = temp[0]
        elif(is_better(temp[1], temp[0])):
            m = temp[1]
        else:
            flag = 0

    if(flag == 0):
        print("no")
    else:
        print("yes")
