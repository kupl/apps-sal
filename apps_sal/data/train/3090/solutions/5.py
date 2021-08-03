def find_2nd_largest(arr):
    res = [arr[i] for i in range(0, len(arr)) if isinstance(arr[i], int)]
    res.sort(reverse=True)
    if len(set(arr)) == 1:
        return None
    else:
        return res[1]
