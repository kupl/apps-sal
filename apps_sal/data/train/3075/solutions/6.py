def count_inversions(array):
    return sum([1 for i in range(len(array)) for j in range(i + 1, len(array)) if array[i] > array[j]])
