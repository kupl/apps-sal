def multiple_of_index(arr):
    result = []
    for (i, j) in enumerate(arr):
        try:
            if j % i == 0:
                result.append(j)
        except:
            continue
    return result
