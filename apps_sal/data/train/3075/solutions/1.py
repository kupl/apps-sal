def count_inversions(array):
    return sum(x > y for i,x in enumerate(array) for y in array[i+1:])
