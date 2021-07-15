def billboard(name, price=30):
    if price == 30:
        result = 0
        for i in range(len(name)):
            result += 30
        return result
    else:
        result = 0
        for i in range(len(name)):
            result += price
        return result
