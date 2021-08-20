def summary_ranges(nums):
    (result, start) = ([], float('-inf'))
    for (a, b) in zip([start] + nums, nums + [-start]):
        if b - a > 1:
            result.append((start, a))
            start = b
    return [[f'{a}', f'{a}->{b}'][b > a] for (a, b) in result[1:]]
