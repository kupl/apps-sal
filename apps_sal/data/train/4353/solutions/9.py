def could_be(o, a):
    return all([x in o.split() for x in a.split()]) if a.strip() and o.strip() else False
