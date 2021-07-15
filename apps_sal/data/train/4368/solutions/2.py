def cost(mins):
    price = 0
    print (mins)
    while mins > 0:
        if mins <= 65:
            price += 30
            mins -= 65
        elif mins - 65 > 0:
            price += 10
            mins -= 30
    return price
