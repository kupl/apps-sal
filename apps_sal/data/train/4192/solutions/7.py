def pairwise(arr, n):
    used = []
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == n and (not (i in used or j in used)):
                used.extend([i, j])
    return sum(used)
