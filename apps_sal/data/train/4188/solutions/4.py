def find_dup(arr):
    memo = set()
    return next(x for x in arr if x in memo or memo.add(x))
