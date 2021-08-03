def two_decimal_places(n):

    l = str(n)
    m = l.split(".")

    returning = ""
    if len(m[1]) == 2:
        return n
    elif len(m[1]) > 2:
        returning = round(n, 2)
        return returning
