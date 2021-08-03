def multiple_of_index(arr):
    bigboy = []
    index = 1
    for x in arr[1:]:
        if x % index == 0:
            bigboy.append(x)
        index += 1
    return bigboy
