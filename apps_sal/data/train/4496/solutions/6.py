def hamming_distance(r, s):
    return len([i for i in range(len(r)) if r[i] != s[i]])
