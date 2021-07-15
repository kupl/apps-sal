def product_sans_n(l):
    contains_zeroes = False
    product = 1
    for n in l:
        if n:
            product *= n
        elif not contains_zeroes:
            contains_zeroes = True
        else:
            return [0] * len(l)
    return [0 if n else product for n in l] if contains_zeroes else [product // n for n in l]
