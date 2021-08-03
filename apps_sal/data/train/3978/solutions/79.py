def check_for_factor(base, factor):
    ls = []
    for i in range(1, base + 1):
        if base % i == 0:
            ls.append(i)
    if factor in ls:
        return True
    else:
        return False
