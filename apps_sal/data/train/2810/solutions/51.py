def solve(arr):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    return [sum((1 if i < 26 and alpha[i] == c else 0 for (i, c) in enumerate(w.lower()))) for w in arr]
