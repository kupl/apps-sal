def base_finder(seq):
    digits = set(c for cs in seq for c in cs)
    return int(max(digits)) + 1
