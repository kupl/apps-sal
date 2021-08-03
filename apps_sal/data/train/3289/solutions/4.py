from itertools import count


def motif_locator(sequence, motif):
    if len(motif) > len(sequence):
        return []
    n = len(motif)
    target_hash = sum(map(ord, motif))
    hashish = sum(map(ord, sequence[:n]))
    res = []
    for i in count():
        if hashish == target_hash and sequence[i:i + n] == motif:
            res.append(i + 1)
        if i + n == len(sequence):
            return res
        hashish += ord(sequence[i + n]) - ord(sequence[i])
