def sum_arrays(arrays, shift):
    m = len(arrays)
    n = len(arrays[0])

    result = [0] * (n + shift * (m - 1))

    index = 0
    for a in arrays:
        for element in a:
            result[index] += element
            index += 1
        index += shift - n

    return result
