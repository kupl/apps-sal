from itertools import groupby


def look_and_say_sequence(seq, n):
    if seq == '22':
        return '22'
    for _ in range(1, n):
        seq = ''.join((f'{len(list(b))}{a}' for (a, b) in groupby(seq)))
    return seq
