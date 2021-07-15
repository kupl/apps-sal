def solve(arr):
    return list(set(filter(lambda x: arr.count(x) != arr.count(-x), arr)))[0]
