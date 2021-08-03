def solve(arr):
    unique = []
    arr.reverse()
    for n in arr:
        if n not in unique:
            unique.insert(0, n)

    return unique
