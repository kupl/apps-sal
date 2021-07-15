def solve(arr):
    arr = [s.lower() for s in arr]
    res = [[ord(c)-97 for c in s] for s in arr]
    res = [[subres[i] for i in range(len(subres)) if subres[i] == i] for subres in res]
    return [len(subres) for subres in res]

