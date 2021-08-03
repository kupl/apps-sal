def cuantas(w):
    return sum([1 if i + 1 == ord(v) - ord('a') + 1 else 0 for i, v in enumerate(w.lower())])


def solve(arr):
    return [cuantas(w) for w in arr]
