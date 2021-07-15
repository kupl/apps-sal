def is_divisible_by_6(s):
    x = [s.replace('*', str(i)) for i in range(10)]
    x = [i for i in x if int(i) % 6 == 0]
    x = [i[1:] if i[0] == '0' and len(i) > 1 else i for i in x]
    return x
