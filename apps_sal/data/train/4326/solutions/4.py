def london_city_hacker(journey):
    total = 0.0
    l = []
    for i in range(len(journey)):
        if type(journey[i]) == str:
            total += 2.4
        elif i < len(journey) - 1 and type(journey[i + 1]) == int:
            l.append(journey[i])
            if len(l) == 2:
                total += 1.5
                l = []
        else:
            total += 1.5
            l = []
    total = round(total, 2)
    return '£' + str(total) + '0'
