def super_size(m):
    arr = [int(x) for x in str(m)]
    n = len(arr)
    result = ''
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
    arr.reverse()
    string_new = [str(i) for i in arr]
    result = int(''.join(string_new))
    return result
