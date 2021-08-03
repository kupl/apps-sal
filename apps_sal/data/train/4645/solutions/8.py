def promenade(choices):
    fraction = (1, 1)
    most_recent_L = (1, 0)
    most_recent_R = (0, 1)
    def fraction_add(L, R): return tuple(l + r for l, r in zip(L, R))
    for C in choices:
        if C == "L":
            most_recent_L = fraction
            fraction = fraction_add(most_recent_L, most_recent_R)
        elif C == "R":
            most_recent_R = fraction
            fraction = fraction_add(most_recent_L, most_recent_R)
        else:
            raise ValueError
    return fraction
