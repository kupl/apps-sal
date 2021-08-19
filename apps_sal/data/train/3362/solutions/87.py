def sum_mix(arr):
    total = ''
    new_lst = []
    for i in arr:
        if i == str(i):
            new_lst.append(int(i))
        else:
            new_lst.append(i)
    total = sum(new_lst)
    return total
