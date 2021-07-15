def multiple_of_index(arr):
    return [arr[x] for x in range(1,len(arr)) if x == 0 or arr[x] % x == 0]
