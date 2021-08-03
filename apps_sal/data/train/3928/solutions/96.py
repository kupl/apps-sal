def billboard(name, price=30):
    sum = 0
    for element in name:
        sum += price
    return sum
