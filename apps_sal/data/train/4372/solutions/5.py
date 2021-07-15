def lostSheep(friday,saturday,total):
    fritag = 0
    for number in friday:
        fritag = fritag + number
    samstag = 0
    for number in saturday:
        samstag = samstag + number
    return int(str(total)) - (fritag + samstag)


