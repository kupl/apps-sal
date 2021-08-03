def solve(arr):
    result = []
    return [sum([0 if y - ord(x[y].lower()) + 97 else 1 for y in range(len(x))]) for x in arr]
