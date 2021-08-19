def solve(arr):
    res = []
    for first in (arr[0] - 1, arr[0], arr[0] + 1):
        for second in (arr[1] - 1, arr[1], arr[1] + 1):
            (val, step, count) = (second, second - first, abs(arr[0] - first) + abs(arr[1] - second))
            for current in arr[2:]:
                val += step
                if abs(val - current) > 1:
                    break
                count += abs(val - current)
            else:
                res.append(count)
    return min(res, default=-1)
