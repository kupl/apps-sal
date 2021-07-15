def modified_sum(lst, p):
    return sum(n**p - n for n in lst)
