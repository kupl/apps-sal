def min_value(lst):
    min_num = ''
    min_lst = []
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                (lst[j + 1], lst[j]) = (lst[j], lst[j + 1])
    for i in range(len(lst)):
        if lst[i] not in min_lst:
            min_lst.append(lst[i])
    for i in min_lst:
        min_num += str(i)
    return int(min_num)
