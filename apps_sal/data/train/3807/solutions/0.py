def smaller(arr):
    # Good Luck!
    return [len([a for a in arr[i:] if a < arr[i]]) for i in range(0, len(arr))]
