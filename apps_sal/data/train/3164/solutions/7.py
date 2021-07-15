def group_by_commas(n):
    if n < 0:
        if n >= -999:
            return str(n)
    elif n <= 999:
        return str(n)
    return format(n, ',')
