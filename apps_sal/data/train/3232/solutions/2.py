def length_of_sequence(arr,n):
    indexes = [i for i,s in enumerate(arr) if s == n]
    if len(indexes) != 2:
        return 0
    else:
        return indexes[-1] - indexes[0] + 1
