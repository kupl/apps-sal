def bumps(road):
    count = 0
    for i in road:
        if i == 'n':
            count += 1
        else:
            pass
    if count > 15:
        return ("Car Dead")
    else:
        return ("Woohoo!")
