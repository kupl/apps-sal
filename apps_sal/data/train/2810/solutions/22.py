def solve(arr):
    return [sum((1 for i in range(len(w)) if ord(w[i].lower()) - 96 == i + 1)) for w in arr]
