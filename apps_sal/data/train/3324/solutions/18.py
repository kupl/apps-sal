def sale_hotdogs(n):
    discount = 0
    if n >= 5 and n < 10:
        discount = 5
    elif n >= 10:
        discount = 10
    return (100 - discount) * n
