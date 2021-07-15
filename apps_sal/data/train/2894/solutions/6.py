def triple_trouble(one, two, three):
    a = one.split(" ")
    a = map(lambda x, y, z: x + y + z, one, two, three)
    return "".join(a)
