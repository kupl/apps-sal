def or_arrays(arr1, arr2, n=0):

    result = []

    for i in range(max(len(arr1), len(arr2))):

        a = b = n

        if i < len(arr1):
            a = arr1[i]

        if i < len(arr2):
            b = arr2[i]

        result.append(b | a)

    return result
