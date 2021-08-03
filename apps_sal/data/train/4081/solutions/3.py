def first_tooth(arr):
    l = len(arr)
    lst = [(arr[i] - arr[i - 1] if i else 0) + (arr[i] - arr[i + 1] if i < l - 1 else 0) for i in range(l)]
    m = max(lst)
    return lst.index(m) if lst.count(m) == 1 else -1
