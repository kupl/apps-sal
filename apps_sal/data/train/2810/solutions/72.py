import string


def solve(arr):
    return [sum((ch == string.ascii_lowercase[i] for (i, ch) in enumerate(word.lower()[:26]))) for word in arr]
