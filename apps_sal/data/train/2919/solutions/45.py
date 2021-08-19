def encode(m, k):
    return [ord(d) - ord('a') + 1 + int(str(k)[i % len(str(k))]) for (i, d) in enumerate(m)]
