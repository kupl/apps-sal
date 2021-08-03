def balanced_num(n):

    total_lst = [i for i in str(n)]
    if len(total_lst) == 1 or len(total_lst) == 2:
        return "Balanced"
    break_even = int(len(total_lst) / 2 - 1)
    break_odd = int(len(total_lst) // 2)
    if len(total_lst) % 2 == 0:
        lst1 = [i for i in total_lst[0:break_even]]
        lst2 = [i for i in total_lst[-break_even:]]
    else:
        lst1 = [i for i in total_lst[0:break_odd]]
        lst2 = [i for i in total_lst[-(break_odd):]]

    for i in range(0, len(lst1)):
        lst1[i] = int(lst1[i])
    for i in range(0, len(lst2)):
        lst2[i] = int(lst2[i])
    a = sum(lst1)
    b = sum(lst2)
    if a == b:
        return "Balanced"

    else:
        return "Not Balanced"
