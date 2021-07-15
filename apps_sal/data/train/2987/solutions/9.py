def is_divide_by(num, *n):
    return not any([num%x for x in n])
