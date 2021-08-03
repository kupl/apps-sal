import math


def count_perms(matrix):
    freq = dict()
    for sub_matrix in matrix:
        for elem in sub_matrix:
            if freq.get(elem) is not None:
                freq[elem] = freq[elem] + 1
            else:
                freq[elem] = 1
    denominator = 1
    for frequency in freq.values():
        denominator = denominator * math.factorial(frequency)
    return math.factorial(sum(freq.values())) / denominator
