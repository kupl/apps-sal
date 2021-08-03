from collections import defaultdict, Counter


def char_freq(message):
    my_dict = {}
    for letter in message:
        my_dict[letter] = my_dict.get(letter, 0) + 1
    return my_dict
