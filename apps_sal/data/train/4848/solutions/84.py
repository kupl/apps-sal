def char_freq(message):
    freq = {}
    for c in message:
        if not c in freq:
            freq[c] = 0
        freq[c] += 1
    return freq
