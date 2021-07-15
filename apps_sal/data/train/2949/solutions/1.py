def split_and_add(arr, n):
    for _ in range(n):
        half = len(arr) // 2
        arr = [a+b for a, b in zip([0] * (len(arr)%2) + arr[:half], arr[half:])]
    
    return arr
