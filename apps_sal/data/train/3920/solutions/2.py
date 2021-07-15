def hamming_distance(a, b):
    return sum(int(i) for i in bin(a^b)[2:])
