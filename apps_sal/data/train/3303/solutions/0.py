def div_con(lst):
    return sum(n if isinstance(n, int) else -int(n) for n in lst)
