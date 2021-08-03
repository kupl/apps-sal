def multiple_of_index(arr):
    results = []
    i = 0
    for elem in arr:
        if i > 0 and elem % i == 0:
            results.append(elem)
        i += 1
    return results
