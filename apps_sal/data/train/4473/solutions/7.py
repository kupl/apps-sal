(a, e, t, m) = ([0, 314], 314, 314, 0.25)
for i in range(2, 170):
    x = int(e * (1 + m))
    t += x
    a.append(t)
    e = x
    if not (i + 1) % 10:
        m -= 0.01
a[-1] = 769832696988485


def xp_to_target_lvl(e=None, lvl=None):
    try:
        if e < 0 or lvl < 1:
            return 'Input is invalid.'
        if lvl == 1 or e >= a[max(lvl - 1, 0)]:
            return f'You have already reached level {lvl}.'
        return a[lvl - 1] - e
    except:
        return 'Input is invalid.'
