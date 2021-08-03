def hamming_distance(a, b):
    result = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            result += 1
    return result
