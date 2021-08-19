test_case = int(input())
while test_case > 0:
    test_case -= 1
    n = int(input())
    arr = [int(x) for x in input().split()]
    c = list()
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
            # c = max(c,temp)
            c.append(temp)
            temp = 0
            flag = True
    # if c % 2 == 0 :
    #     print("No")
    # else:
    #     print("Yes")
    c.append(temp)
    max1 = max(c)
    c.remove(max1)
    max2 = max(c)
    if max1 % 2 == 0 or (max1 / 2 + (max1 & 1)) < max2:
        print("No")
    else:
        print("Yes")
