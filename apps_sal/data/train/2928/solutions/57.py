def alphabet_war(fight):
    count = 0
    left_power = dict(w=4, p=3, b=2, s=1)
    right_power = dict(m=4, q=3, d=2, z=1)
    for l in fight:
        if l in left_power:
            count += left_power[l]
        elif l in right_power:
            count -= right_power[l]
    if count < 0:
        return 'Right side wins!'
    if count > 0:
        return 'Left side wins!'
    elif count == 0:
        return "Let's fight again!"
