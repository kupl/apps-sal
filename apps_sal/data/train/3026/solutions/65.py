def min_value(digits):
    list =[]
    list2 =[]
    ans = ""
    for i in digits:
        if i not in list:
            list.append(i)
            list2 = sorted(list)
    for i in list2:
        ans = ans +str(i)
    return int(ans)
