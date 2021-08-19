def sea_sick(sea):
    waves = sum((sea[i:i + 2] in '_~_' for i in range(len(sea) - 1)))
    if waves / float(len(sea)) > 0.2:
        return 'Throw Up'
    return 'No Problem'
