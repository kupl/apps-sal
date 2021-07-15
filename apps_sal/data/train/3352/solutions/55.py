def find_longest(arr):
    return [x for x in arr if len(str(x)) == len(str(sorted(arr)[-1]))][0]
