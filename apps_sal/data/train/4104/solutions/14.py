def max_tri_sum(numbers):
    s = sorted(set(numbers), reverse=True)
    return s[0]+s[1]+s[2]
