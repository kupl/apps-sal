elevator = lambda l, r, c: ("right", "left")[abs(c - l) < abs(c - r)]
