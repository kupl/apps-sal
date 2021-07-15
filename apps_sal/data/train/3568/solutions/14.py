def bumps(road):
    L = list(road)
    C = L.count('n')
    if C > 15:
        return 'Car Dead'
    else:
        return 'Woohoo!'

