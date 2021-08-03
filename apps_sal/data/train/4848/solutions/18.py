from collections import defaultdict


def char_freq(message):
    frequency = defaultdict(lambda: 0)
    for letter in list(message):
        frequency[letter] += 1
    return frequency
