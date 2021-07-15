def solve(arr):
    return list(set([x for x in arr if -x not in arr]))[0]
