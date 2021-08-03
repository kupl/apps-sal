def billboard(name, price=30):
    result = 0
    for letter in name:
        result += price
    return result
