def find_longest(arr):
    for i in arr:
        if len(str(i)) >= len(str(max(arr))):
            return i
