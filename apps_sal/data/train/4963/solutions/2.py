def closest_multiple_10(i):
    r = i % 10
    return i - r if r < 5 else i - r + 10
