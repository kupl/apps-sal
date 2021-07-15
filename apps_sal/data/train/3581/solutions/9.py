def sea_sick(sea):
    c,p = 0,sea[0]
    for s in sea[1:]:
        if s != p:
            c += 1
        p = s
    return 'Throw Up' if c/len(sea) > 0.2 else 'No Problem'
