def men_still_standing(cards):
    a = {'n': 11}
    b = {'n': 11}
    for x in cards:
        jg(a if x[0] == 'A' else b, x)
        if a['n'] < 7 or b['n'] < 7:
            break
    return (a['n'], b['n'])


def jg(t, x):
    o = t.get(x[1:-1])
    if o == 1:
        t[x[1:-1]] = -1
        t['n'] -= 1
    elif o == None:
        if x[-1] == 'R':
            t[x[1:-1]] = -1
            t['n'] -= 1
        if x[-1] == 'Y':
            t[x[1:-1]] = 1
