def alphabet_war(fight):
    left_side = 'wpbs'
    right_side = 'mqdz'
    left_power = 0
    right_power = 0
    bombs = [i for i in range(0, len(fight)) if fight[i] == '*']
    death = []
    for boom in bombs:
        if 0 < boom < len(fight) - 1:
            death.append(boom - 1)
            death.append(boom + 1)
        elif boom == 0:
            death.append(boom + 1)
        elif boom == len(fight) - 1:
            death.append(boom - 1)
    bombs_and_death = bombs + death
    after_fight = ''.join((fight[i] if i not in bombs_and_death else '' for i in range(0, len(fight))))
    for i in after_fight:
        if i == 'w' or i == 'm':
            pow = 4
        elif i == 'p' or i == 'q':
            pow = 3
        elif i == 'b' or i == 'd':
            pow = 2
        elif i == 's' or i == 'z':
            pow = 1
        if i in left_side:
            left_power += pow
        elif i in right_side:
            right_power += pow
    if left_power > right_power:
        return 'Left side wins!'
    elif right_power > left_power:
        return 'Right side wins!'
    else:
        return "Let's fight again!"
