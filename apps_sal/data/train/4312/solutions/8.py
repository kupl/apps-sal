import re


def pick_peaks(arr):
    slope = ''.join(('u' if b > a else 'd' if a > b else 'p' for (a, b) in zip(arr, arr[1:])))
    positions = [m.start() + 1 for m in re.finditer('up*d', slope)]
    peaks = [arr[pos] for pos in positions]
    return {'pos': positions, 'peaks': peaks}
