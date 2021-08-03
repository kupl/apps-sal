def fix_progression(arr):
    best = len(arr) - 2
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if (arr[j] - arr[i]) % (j - i) != 0:
                continue
            step = (arr[j] - arr[i]) // (j - i)
            wrongs = sum(1 for k in range(len(arr)) if arr[k] != arr[i] + (k - i) * step)
            best = min(wrongs, best)
            if best < i - 2:
                break
    return best
