def bouncy_ratio(percent):
    if percent < 0 or percent > 0.99:
        raise Error
    n = 99
    bouncy = 0.0
    while True:
        n += 1
        ns = str(n)
        gaps = [int(ns[i]) - int(ns[i - 1]) for i in range(1, len(ns))]
        if not(all(gap >= 0 for gap in gaps) or all(gap <= 0 for gap in gaps)):
            bouncy += 1.0
            if bouncy / n >= percent:
                return n
