def contamination(t, char):
    return t.translate({ord(x):char for x in t})
