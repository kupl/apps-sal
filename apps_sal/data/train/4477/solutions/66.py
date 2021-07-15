def reverse_number(n):
    n = str(n)
    if "-" == n[0]:
        n = n[1:]
        n = n[::-1]
        n = "-" + n
    else:
        return int(n[::-1])
    return int(n)
