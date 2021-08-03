def minimum(arr):
    smol = 1000
    for i in range(0, len(arr)):
        if arr[i] < smol:
            smol = arr[i]

    return smol


def maximum(arr):
    beeg = 0
    for i in range(0, len(arr)):
        if arr[i] > beeg:
            beeg = arr[i]

    return beeg
