def find_longest(arr):
    for x in arr:
        if x == max(arr, key = lambda n: len(str(n))):
            return x
