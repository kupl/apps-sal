def solve(arr):
    return [x for x in arr if not -x in arr][0]
