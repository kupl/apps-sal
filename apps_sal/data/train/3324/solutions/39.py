def sale_hotdogs(n):
    # your code here
    price = 0
    if n >= 0 and n < 5:
        price = n * 100
    elif n >= 5 and n < 10:
        price = n * 95
    else:
        price = 90 * n
    return price
