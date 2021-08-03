def find_dup(arr):
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] == arr[j]:
                return arr[i]
    return None
