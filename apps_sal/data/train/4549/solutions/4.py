def text(green, blue):
    if green:
        return "Green wins: {0}".format(' '.join(str(x) for x in green))
    elif blue:
        return "Blue wins: {0}".format(' '.join(str(x) for x in blue))
    return 'Green and Blue died'


def lemming_battle(battlefield, green, blue):
    green, blue = sorted(green, reverse=True), sorted(blue, reverse=True)
    if not green or not blue:
        return text(green, blue)
    for i in range(battlefield):
        try:
            res = green[i] - blue[i]
            if res == 0:
                blue[i] = False
                green[i] = False
            elif res > 0:
                green[i] = res
                blue[i] = False
            else:
                blue[i] = abs(res)
                green[i] = False
        except IndexError:
            break
    return lemming_battle(battlefield, [x for x in green if x], [x for x in blue if x])
