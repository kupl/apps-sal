def nth_smallest(arr, pos):
    # your code here
    minimum = 0
    for i in range(pos):
        minimum = minimum_k(arr)

    return minimum


def minimum_k(array):

    minimum = 99999

    for i in array:
        minimum = min(minimum, i)

    array.remove(minimum)

    return minimum
