def find_longest(arr):
    for i in sorted(arr, key=lambda x: len(str(x))):
        if len(str(i)) == max(len(str(i)) for i in arr):
            return i
