def solve(arr):
    l = sorted(arr)
    result = []
    while l:
        result.append(l.pop())
        l.reverse()
    return result
