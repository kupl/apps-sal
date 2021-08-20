def button_sequences(r, b):
    (r_on, b_on) = (False, False)
    res = ''
    for i in range(len(r)):
        (ri, bi) = (int(r[i]), int(b[i]))
        if not r_on | b_on:
            if ri:
                res += 'R'
                r_on = True
            elif bi:
                res += 'B'
                b_on = True
        elif r_on:
            if not ri:
                r_on = False
                if bi:
                    b_on = True
                    res += 'B'
        elif b_on:
            if not bi:
                b_on = False
                if ri:
                    r_on = True
                    res += 'R'
    return res
