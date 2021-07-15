def first_non_consecutive(arr):
    n = 0
    try:
        for i in arr:
            if i + 1 == arr[n + 1]:
                n += 1
                continue
            elif i + 1 != arr[n + 1]:
                return arr[n + 1]
    except:
        return None
