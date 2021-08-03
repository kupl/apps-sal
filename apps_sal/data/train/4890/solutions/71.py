def volume(lens):
    return lens[0] * lens[1] * lens[2]


def find_difference(a, b):
    return abs(volume(a) - volume(b))
