def solve(arr):
    arr.sort(reverse=True)
    return [arr.pop(-(i % 2)) for i in range(len(arr))]
