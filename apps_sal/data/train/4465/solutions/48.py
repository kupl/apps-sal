def super_size(n):
    arr = [x for x in str(n)]
    arr.sort(reverse = True)
    return int(''.join(arr))
