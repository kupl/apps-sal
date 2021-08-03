def alphabet_war(fight):
    l = {'w': 4, 'p': 3, 'b': 2, 's': 1, 'm': -4, 'q': -3, 'd': -2, 'z': -1}
    a = 0
    for i in list(fight):
        a += 0 if i in 'acefghijklnortuvxy' else l[i]
    return "Let's fight again!" if a == 0 else ('Right ' if a < 0 else 'Left ') + 'side wins!'
