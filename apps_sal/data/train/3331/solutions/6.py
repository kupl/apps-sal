def solve(arr, n):
    caught = []
    for d in [idx for idx in range(len(arr)) if arr[idx] == 'D']:
        for c in [idx for idx in range(len(arr)) if arr[idx] == 'C']:
            if c in range(d - n, d + n + 1) and c not in caught:
                caught += [c]
                break
    return len(caught)
