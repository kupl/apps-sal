def crap(garden, bags, cap):
    count_crap = 0
    for x in garden:
        for y in x:
            if y == 'D':
                return 'Dog!!'
            if y == '@':
                count_crap += 1
    if bags * cap >= count_crap:
        return 'Clean'
    else:
        return 'Cr@p'
