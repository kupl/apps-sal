def find_missing_number(sequence):
    arr = sequence.split(' ')
    if arr == ['']:
        return 0
    for i in range(0, len(arr)):
        try:
            arr[i] = int(arr[i])            
        except ValueError:
            return 1
    c = 1
    while c in arr:
        c += 1
    if c > max(arr):
        return 0
    return c
