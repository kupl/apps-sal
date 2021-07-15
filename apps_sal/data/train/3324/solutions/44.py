def sale_hotdogs(n):
    if n < 5:
        bill = 100
    elif n < 10:
        bill = 95
    else:
        bill = 90
    return n * bill
