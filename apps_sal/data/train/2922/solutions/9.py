def crap(garden, bags, cap):
    for each in garden:
        for i in each:
            if i == 'D':
                return 'Dog!!'
    count = 0
    for each in garden:
        for i in each:
            if i == '@':
                count += 1
    count_caps = bags * cap
    if count > count_caps:
        return 'Cr@p'
    else:
        return "Clean"
