def hotpo(zahl):
    count = 0
    while zahl > 1:
        count += 1
        if zahl % 2 == 0:
            zahl = zahl / 2
        else:
            zahl = 3 * zahl + 1
    return count
