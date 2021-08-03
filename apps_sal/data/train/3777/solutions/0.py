from string import ascii_uppercase

values = {x: i for i, x in enumerate(ascii_uppercase, 1)}


def quicksum(packet):
    return sum(values.get(c, 0) * i for i, c in enumerate(packet, 1)) * all(c.isspace() or c.isupper() for c in packet)
