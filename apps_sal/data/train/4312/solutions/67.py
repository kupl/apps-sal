import operator


def pick_peaks(arr):
    pos = []
    peaks = []
    if len(arr) < 3:
        return {"pos": [], "peaks": []}

    # substract
    diff = list(map(operator.sub, arr[1:], arr[:-1]))

    # deal with plateue
    for i in range(len(diff) - 1, 0, -1):
        if diff[i - 1] == 0:
            diff[i - 1] = diff[i]

    # find peaks
    def is_peak(a, b): return 1 if a * b < 0 and a > b else 0
    muld = list(map(is_peak, diff[:-1], diff[1:]))

    # get positions
    pos = [i + 1 for i, v in enumerate(muld) if v == 1]

    # get peaks
    for i in pos:
        peaks.append(arr[i])

    return {"pos": pos, "peaks": peaks}
