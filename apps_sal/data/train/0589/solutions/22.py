for _ in range(int(input())):
    string = input()
    count = 0
    list1 = []
    for i in string:
        if i == '.':
            count += 1
        elif count != 0:
            list1.append(count)
            count = 0
    if len(list1) == 0:
        print(0)
    else:
        ans = 1
        count = list1[0]
        for a in list1:
            if a > count:
                ans += 1
                count = a
        print(ans)
