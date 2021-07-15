def order_weight(strng):
    sum_sort = lambda x: sum([int(n) for n in x])
    return ' '.join(sorted(sorted(strng.split()), key=sum_sort))
