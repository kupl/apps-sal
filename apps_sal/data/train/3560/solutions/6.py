def ski_jump(mountain):
    k = 0
    l = 0
    m = 0
    for i in mountain:
        i = mountain[k]
        k += 1
    l = k * 1.5
    m = k * l * 9 / 10
    if m < 10:
        m = '%.2f' % m
        m = str(m)
        m = m + " metres: He's crap!"
        return m
    elif m >= 10 and m <= 25:
        m = '%.2f' % m
        m = str(m)
        m = m + " metres: He's ok!"
        return m
    elif m >= 25 and m <= 50:
        m = '%.2f' % m
        m = str(m)
        m = m + " metres: He's flying!"
        return m
    else:
        m = '%.2f' % m
        m = str(m)
        m = m + ' metres: Gold!!'
        return m
