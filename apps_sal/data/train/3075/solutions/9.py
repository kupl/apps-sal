def count_inversions(array):
    inversions = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                inversions += 1
    return inversions
