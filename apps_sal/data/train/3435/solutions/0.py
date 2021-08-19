import re
powers = {'w': -4, 'p': -3, 'b': -2, 's': -1, 'm': +4, 'q': +3, 'd': +2, 'z': +1}


def alphabet_war(fight):
    fight = re.sub('.(?=\\*)|(?<=\\*).', '', fight)
    result = sum((powers.get(c, 0) for c in fight))
    if result < 0:
        return 'Left side wins!'
    elif result > 0:
        return 'Right side wins!'
    else:
        return "Let's fight again!"
