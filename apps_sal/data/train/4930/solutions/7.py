from itertools import combinations


def find_zero_sum_groups(arr, n):
    if not arr:
        return 'No elements to combine'
    else:
        results = [list(x) for x in combinations(sorted(set(arr)), n) if sum(x) == 0]
        if not results:
            return 'No combinations'
        elif len(results) == 1:
            return results[0]
        else:
            return results
