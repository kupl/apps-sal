def solve(arr):
    alpha = [chr(i) for i in range(ord('a'), ord('z') + 1, 1)]
    lst = []
    for item in arr:
        lst.append(sum([x.lower() == y.lower() for (x, y) in zip(alpha, item)]))
    return lst
