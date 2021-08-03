def reverse_number(n):
    if n < 0:
        n = str(n)
        n = n[::-1]
        return -1 * int(n.replace('-', ''))
    else:
        n = str(n)
        n = n[::-1]
        return int(n)
