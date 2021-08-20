def rank_of_element(lst, i):
    return sum((n <= lst[i] for n in lst[:i])) + sum((n < lst[i] for n in lst[i + 1:]))
