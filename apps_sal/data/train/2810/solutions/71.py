import string


def solve(arr):
    return [sum((ch == string.ascii_lowercase[i] for (i, ch) in enumerate(word[:26].lower()))) for word in arr]
