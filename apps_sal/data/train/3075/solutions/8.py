def fun1(a1, a2):
    return sum([1 if a1 > i else 0 for i in a2])


def count_inversions(array):
    s = 0
    for i in range(len(array)):
        if i != len(array) - 1:
            s += fun1(array[i], array[i + 1:])
    return s
