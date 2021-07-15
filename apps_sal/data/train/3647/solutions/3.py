def solve(arr):
    rarr = sorted(arr, reverse=True)
    farr = rarr[::-1]
    return [item for sublist in zip(rarr, farr) for item in sublist][:len(rarr)]
