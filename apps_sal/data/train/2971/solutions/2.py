def watch_pyramid_from_the_side(c, i=1, acc=[]):
    if c == None:
        return c
    if not c:
        return '\n'.join(acc)
    return watch_pyramid_from_the_side(c[:-1], i + 2, [' ' + l + ' 'for l in acc] + [c[-1] * i])


def watch_pyramid_from_above(c, i=1, acc=[]):
    if c == None:
        return c
    if not c:
        return '\n'.join(acc)
    return watch_pyramid_from_above(c[:-1], i + 2, [c[-1] * i] + [c[-1] + l + c[-1] for l in acc] + [c[-1] * i] * bool(acc))


def count_visible_characters_of_the_pyramid(c):
    return c and (2 * len(c) - 1)**2 or -1


def count_all_characters_of_the_pyramid(c):
    return c and (4 * len(c)**3 - len(c)) // 3 or -1
