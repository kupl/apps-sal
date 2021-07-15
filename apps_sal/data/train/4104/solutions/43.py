def max_tri_sum(numbers):
    setnum = set(numbers)
    lst = list(setnum)
    lst_sort = sorted(lst)
    return sum(lst_sort[-3:])

