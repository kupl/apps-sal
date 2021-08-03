def mcd(fraccion):
    if fraccion[0] % fraccion[1] == 0:
        return fraccion[1]
    else:
        return mcd((fraccion[1], fraccion[0] % fraccion[1]))


def reduce_fraction(fraccion):
    return (fraccion[0] // mcd(fraccion), fraccion[1] // mcd(fraccion))
