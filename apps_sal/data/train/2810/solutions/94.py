from string import ascii_lowercase

def solve(arr):
    return [sum(c1 == c2 for c1, c2 in zip(s.lower(), ascii_lowercase)) for s in arr]
