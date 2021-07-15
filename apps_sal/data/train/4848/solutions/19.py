def char_freq(message):
    unique = set(message)
    freq = dict(list(zip(unique, [0]*len(unique))))
    for s in message:
        freq[s] += 1
    return freq

