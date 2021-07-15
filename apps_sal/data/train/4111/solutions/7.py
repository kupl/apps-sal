def sabb(s, value, happiness):
    sab = []
    for x in s:
        if x == 's' or x == 'a' or x == 'b' or x == 't' or x == 'i' or x == 'c' or x == 'l':
            sab.append(1)
        else: 
            sab.append(0)
    z = sum(sab)
    y = z + value + happiness
    if y <= 22:
        return 'Back to your desk, boy.'
    else:
        return 'Sabbatical! Boom!'
