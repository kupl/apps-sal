from itertools import cycle, islice


def endless_string(string, start, length):
    i = (start + (length + 1 if length < 0 else 0)) % len(string)
    return ''.join(islice(cycle(string), i, i + abs(length)))
