def directions(goal):
    count = lambda s: len([c for c in goal if c == s])
    ns = 1 * count("N") - 1 * count("S")
    we = 1 * count("W") - 1 * count("E")
    ns = [("N" if ns > 0 else "S")] * abs(ns)
    we = [("W" if we > 0 else "E")] * abs(we)
    return ns + we

