def solve(arr):
    res = []
    for word in arr:
        count = 0
        for i, c in enumerate(word.lower()):
            if ord(c) - 97 == i: count += 1
        res.append(count)
    return res
