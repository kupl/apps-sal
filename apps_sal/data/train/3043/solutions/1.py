def print_nums(*num):
    return '\n'.join([str(x).zfill(len(str(max(num)))) for x in num])
