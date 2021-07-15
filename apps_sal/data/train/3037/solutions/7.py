def obtain_max_number(arr):
    used = [False] * len(arr)
    i = 0
    while i < len(arr):
        if not used[i]:
            j = i + 1
            while j < len(arr):
                if arr[j] == arr[i]:
                    arr[j] += arr[i]
                    arr[i] = 0
                    used[i] = True
                    i = -1
                    break
                j += 1
        i += 1
    return max(arr)

