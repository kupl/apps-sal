get = dict(zip("ATCG", "TAGC")).__getitem__


def reverse_complement(dna):
    try:
        return ''.join(map(get, reversed(dna)))
    except KeyError:
        return "Invalid sequence"
