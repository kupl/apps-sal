def pick_me(arr):
    plateau = None

    for i, p in enumerate(arr[1:-1]):
        if arr[i] < p > arr[i + 2]:
            yield(i + 1, p)
            plateau = None

        if arr[i] < p == arr[i + 2]:
            plateau = (i + 1, p)

        if plateau and arr[i] == p > arr[i + 2]:
            yield plateau
            plateau = None


def pick_peaks(arr):
    picked = list(zip(*pick_me(arr)))
    pos, peaks = picked if picked else ([], [])

    return {
        "pos": list(pos),
        "peaks": list(peaks)
    }
