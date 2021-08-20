def max_tri_sum(numbers):
    numbers_lst = []
    for i in numbers:
        if i not in numbers_lst:
            numbers_lst.append(i)
            numbers_lst.sort()
    return sum(numbers_lst[-3:])
