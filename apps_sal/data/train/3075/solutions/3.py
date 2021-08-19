def count_inversions(array):
    n = len(array)
    return sum([1 for i in range(n) for j in range(n) if i < j and array[i] > array[j]])
