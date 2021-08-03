def fix_progression(arr):
    min_c = len(arr)
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if (arr[j] - arr[i]) % (j - i) != 0:
                continue
            a = (arr[j] - arr[i]) // (j - i)
            c = 0
            for k in range(len(arr)):
                if arr[i] + (k - i) * a != arr[k]:
                    c += 1
            if c < min_c:
                min_c = c
    return min_c
