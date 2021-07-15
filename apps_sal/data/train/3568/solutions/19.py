def bumps(road):
    road.count('n')
    if road.count('n') <= 15:
        return "Woohoo!"
    elif road.count('n') > 15:
        return  "Car Dead"
    else:
        pass

