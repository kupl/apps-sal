from itertools import cycle, islice


def endless_string(string, start, length):
    r = (start + (length + 1) * (length < 0)) % len(string)
    return ''.join(islice(cycle(string), r, r + abs(length)))
