def multiple_of_index(arr):
    print(arr)
    return [arr[i] for i in range(1, len(arr)) if not arr[i] % i ]
