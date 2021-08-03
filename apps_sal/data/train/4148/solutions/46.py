def sum_digits(number):
    # ...
    q = 0
    h = str(number.__abs__())
    for i in h:
        q += int(i)

    return q
