def sum_str(a, b):
    if len(a) == 0 and len(b) == 0: return '0'
    if len(a) == 0: return b
    if len(b) == 0: return a
    sum = int(a) + int(b)
    return str(sum)
