def bumps(road):
    nr_bumps = 0
    for c in road:
        if c == 'n':
            nr_bumps += 1
    return "Woohoo!" if nr_bumps < 16 else "Car Dead"
