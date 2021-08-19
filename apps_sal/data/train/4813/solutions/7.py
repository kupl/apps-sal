def get_num(n):
    return sum(((d in '0689') + (d == '8') for d in str(n)))
