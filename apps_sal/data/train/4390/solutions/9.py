def fly_by(lamps, drone):

    #  <----  hack the lamps!

    x = len(lamps)
    o = min(len(drone), x)
    x = (x - o) * 'x'
    o = o * 'o'

    return (
        o + x,  # concatenation

        ''.join((o, x)),  # join

        "%s%s" % (o, x),  # C-style

        "{}{}".format(o, x),  # function

        f"{o}{x}"  # f-string

    )[__import__('random').randint(0, 4)]
