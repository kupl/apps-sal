def past(h, m, s):
    return sum([ h * 60 * 60 * 1000,
             m * 60 * 1000,
             s * 1000 ])
