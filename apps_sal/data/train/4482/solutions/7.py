def even_numbers_before_fixed(s, fe):
    if fe in s:
        idx = s.index(fe)
        return sum([(e+1)%2 for e in s[:idx]])
    else:
        return -1
