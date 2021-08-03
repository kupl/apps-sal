from collections import Counter


def fix_progression(arr):
    params = Counter()
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[j] - arr[i]) % (j - i) == 0:
                d = (arr[j] - arr[i]) // (j - i)
                s = arr[i] - i * d
                params[(s, d)] += 1

    start, diff = params.most_common(1)[0][0]

    count = 0
    for i in range(len(arr)):
        if arr[i] != start + i * diff:
            count += 1
    return count
