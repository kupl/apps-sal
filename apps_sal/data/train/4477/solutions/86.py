def reverse_number(n):
    if n < 0:
        a = str(n)[1:]
        return int('{}{}'.format(str(n)[0], a[::-1]))
    else:
        return int(str(n)[::-1])
