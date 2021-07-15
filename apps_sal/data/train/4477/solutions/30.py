def reverse_number(n):
    l_1 = str(n)
    if l_1[0] == '-':
        return int(l_1[0]+l_1[:0:-1])
    else:
        return int(l_1[::-1])
