def solve(arr):
    return list(map(lambda a: sum(i == ord(x) - 96 for i, x in enumerate(a.lower(), 1)), arr))
