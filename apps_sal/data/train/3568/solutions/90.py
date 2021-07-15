def bumps(road):
    newrd = list(road)
    bumps = newrd.count('n')
    if bumps <= 15:
        return "Woohoo!"
    elif bumps > 15:
        return "Car Dead"
       

