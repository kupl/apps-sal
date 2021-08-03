from itertools import chain, repeat

alpha = 'abcdefghijklmnopqrstuvwxyz'


def encode(message, key):
    message_l = [(alpha.index(c) + 1) for c in message]
    key_l = [i for i in chain.from_iterable(repeat([int(num) for num in str(key)], 100))]
    return [(message_l[i] + key_l[i]) for i in range(len(message_l))]
