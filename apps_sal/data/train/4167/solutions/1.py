def pair_apply(a, fn):
    """
    Apply a funtion to each pair of consecutive 
    values in the array and return the resultant array
    """
    return [fn(x, y) for (x, y) in zip(a, a[1:])]


def run_length_encode(a):
    """Run length encode the given array"""
    a = [(x, 1) for x in a]
    i = 0
    while i < len(a) - 1:
        if a[i][0] == a[i + 1][0]:
            a[i] = (a[i][0], a[i][1] + 1)
            del a[i + 1]
        else:
            i += 1
    return a


def descriptions(arr):
    """
    Caluculate number of possible range collapse 
    permutations for givven array
    """
    deltas = pair_apply(arr, lambda x, y: y - x)
    rle_deltas = run_length_encode(deltas)
    result = 1
    for (delta, count) in rle_deltas:
        if delta == 1:
            result *= 2 ** count
    return result
