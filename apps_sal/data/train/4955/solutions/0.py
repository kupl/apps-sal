from operator import mul


def ride(group, comet):

    def val(name):
        return reduce(mul, (ord(c) - 64 for c in name))
    return 'GO' if val(comet) % 47 == val(group) % 47 else 'STAY'
