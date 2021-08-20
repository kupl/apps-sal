def kooka_counter(laughing):
    if len(laughing) == 0:
        return 0
    kooks = 1
    current = laughing[0]
    for i in range(2, len(laughing), 2):
        if laughing[i] != current:
            current = current.swapcase()
            kooks += 1
    return kooks
