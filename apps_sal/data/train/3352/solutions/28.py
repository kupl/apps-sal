def find_longest(arr):
    max = len(str(sorted(arr)[-1]))
    return list(filter(lambda x: len(str(x)) == max, arr))[0]
