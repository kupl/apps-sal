def billboard(name, price=30):
    output = 0
    for i in range(0,len(name)):
        output += price
    return output
