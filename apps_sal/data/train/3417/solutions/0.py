def cut_the_ropes(arr):
    results = [len(arr)]
    while arr:
        m = min(arr)
        arr = [elem - m for elem in arr if elem != m]
        results.append(len(arr))
    return results[:-1]
    

