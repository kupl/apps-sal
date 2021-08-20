def pick_peaks(arr):
    start = 0
    sequence = []
    (ind, val) = ([], [])
    posPeaks = {'pos': [], 'peaks': []}
    from itertools import groupby
    for (key, group) in groupby(arr):
        sequence.append((key, start))
        start += sum((1 for _ in group))
    for ((b, bi), (m, mi), (a, ai)) in zip(sequence, sequence[1:], sequence[2:]):
        if b < m and a < m:
            ind.append(mi)
            val.append(m)
    posPeaks['pos'] = ind
    posPeaks['peaks'] = val
    return posPeaks
