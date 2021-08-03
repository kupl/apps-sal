def billboard(name, price=30):
    num = len(name)
    calc = 0
    count = 0
    while count < num:
        calc = calc + price
        count = count + 1
    return calc
