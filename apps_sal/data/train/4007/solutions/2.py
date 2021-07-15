def finding_k(arr):
    s = set(arr)
    if s == {1}:
        return -1
    for k in range(max(s), 0, -1):
        r = arr[0] % k
        if all(x % k == r for x in s):
            return k
    return -1
    

