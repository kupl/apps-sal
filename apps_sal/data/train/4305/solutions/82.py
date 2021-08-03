def order_weight(strng):
    def sum_sort(x): return sum([int(n) for n in x])
    return ' '.join(sorted(sorted(strng.split()), key=sum_sort))
