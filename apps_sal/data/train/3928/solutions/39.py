def billboard(name, price=30):
    sum = 0
    for char in name:
        sum += price
    return sum
