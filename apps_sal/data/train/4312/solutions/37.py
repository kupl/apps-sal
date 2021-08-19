from itertools import groupby


def pick_peaks(arr):
    start = 0
    sequence = []
    for (key, group) in groupby(arr):
        sequence.append((key, start))
        start += sum((1 for element in group))
    peaks = []
    pos = []
    for ((b, bi), (m, mi), (a, ai)) in zip(sequence, sequence[1:], sequence[2:]):
        if b < m and a < m:
            pos.append(mi)
            peaks.append(m)
    result = {}
    result['pos'] = pos
    result['peaks'] = peaks
    return result
