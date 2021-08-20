def solve(arr):
    return list(set((x for x in arr if x * -1 not in arr)))[0]
