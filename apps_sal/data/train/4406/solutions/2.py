def tram(stops, descending, onboarding):
    (n, m) = (0, 0)
    for (d, u) in zip(descending[:stops], onboarding):
        n += u - d
        m = max(m, n)
    return m
