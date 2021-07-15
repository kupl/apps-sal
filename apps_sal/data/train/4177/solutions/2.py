def men_from_boys(arr):
    odds, evens = [], []
    for x in set(arr): [evens, odds][x%2].append(x)
    return sorted(evens) + sorted(odds)[::-1]
