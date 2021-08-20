from itertools import combinations


def fix_progression(arr):
    ans = len(arr) - 1
    for (l, r) in combinations(range(len(arr)), 2):
        step = (arr[r] - arr[l]) / (r - l)
        if step.is_integer():
            step = int(step)
            changed = sum((a != i for (i, a) in zip(range(arr[l] - step * l, 10 ** 10 * step, step), arr))) if step else sum((a != arr[l] for a in arr))
            ans = min(ans, changed)
    return ans
