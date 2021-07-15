def find_longest(arr):
    return list(filter(lambda x: len(str(x)) == len(str(max(arr))), arr))[0]
