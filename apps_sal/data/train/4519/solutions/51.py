def max_number(n):
    l = int(''.join(x for x in sorted([x for x in str(n)], reverse=True)))
    return l
