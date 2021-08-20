from collections import defaultdict


def char_freq(message):
    char_dict = defaultdict(int)
    for c in message:
        char_dict[c] += 1
    return char_dict
