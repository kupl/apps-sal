def sale_hotdogs(n):
    if n < 5:
        bill = n * 100
    elif n < 10:
        bill = n * 95
    else:
        bill = n * 90
    return bill
