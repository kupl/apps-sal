def fly_by(lamps, drone):

    x = len(lamps)
    o = min(len(drone), x)
    x = (x - o) * 'x'
    o = o * 'o'

    return (
        o + x,

        ''.join((o, x)),

        "%s%s" % (o, x),

        "{}{}".format(o, x),

        f"{o}{x}"

    )[__import__('random').randint(0, 4)]
