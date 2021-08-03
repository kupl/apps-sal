def pairwise(arr, n):
    seen = set()
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == n and not (i in seen or j in seen):
                seen.add(i)
                seen.add(j)
                break
    return sum(seen)
