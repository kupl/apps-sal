def distinct(seq):
    unique_lst = []
    for num in seq:
        if num not in unique_lst:
            unique_lst.append(num)
    return unique_lst
