def get_military_time(t):
    modt = t[:-2]
    if ('12' == t[:2]):
        modt = '00' + modt[2:]
    if ('PM' == t[-2:]):
        modt = str(12 + int(modt[:2])) + modt[2:]
    return modt
