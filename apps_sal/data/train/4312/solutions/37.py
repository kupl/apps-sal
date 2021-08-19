from itertools import groupby


def pick_peaks(arr):
    # remove plateaus using groupby and just remember the first occurrence position
    # build a new list called "sequence"
    start = 0
    sequence = []
    for key, group in groupby(arr):
        sequence.append((key, start))  # adds tuples for key and first occurrence
        start += sum(1 for element in group)  # start plus number of consequtive occurrences

    peaks = []
    pos = []
# b like before tuple(value, original index), m like middle, a like after
    for (b, bi), (m, mi), (a, ai) in zip(sequence, sequence[1:], sequence[2:]):
        if b < m and a < m:
            pos.append(mi)
            peaks.append(m)
# Build result
    result = {}
    result['pos'] = pos
    result['peaks'] = peaks
    return result
