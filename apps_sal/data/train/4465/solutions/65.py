def super_size(n):
    ints = [int(thing) for thing in list(str(n))]
    ints = sorted(ints, reverse=True)
    strings = [str(integ) for integ in ints]
    new_str = ''.join(strings)
    return int(new_str)
