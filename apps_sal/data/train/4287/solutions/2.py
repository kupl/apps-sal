def get_participants(handshakes):
    from math import ceil
    '\n        Person #1 can shake hands with (n-1) people, person #2\n        can shake hands with (n-2) people... etc. Therefore,\n        n people can at most shake hands h = n*(n-1)/2 different times.\n        \n        If we flip this equation we get the amount\n        of people necessary:\n        n = 1/2 +(-) sqrt((8*h + 1)/4)\n        \n        The number of handshakes given might be smaller than\n        the max amount possible for n people, so we need to round up.\n    '
    return ceil(0.5 + ((8 * handshakes + 1) / 4) ** 0.5)
