test_case = int(input())
while test_case > 0:
    test_case -= 1
    n = int(input())
    arr = [int(x) for x in input().split()]
    c = 0
    temp = 0
    times = 0
    flag = True
    for a in arr:
        if a == 0:
            temp += 1
            if flag:
                flag = False
                times += 1
        else:
            c = max(c, temp)
            temp = 0
            flag = True
    if c % 2 == 0:
        print("No")
    else:
        print("Yes")
