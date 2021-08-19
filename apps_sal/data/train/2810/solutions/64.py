def solve(arr):
    result = []
    for s in arr:
        result.append(sum((1 for (i, c) in enumerate(s.lower()) if ord(c) - 97 == i)))
    return result
