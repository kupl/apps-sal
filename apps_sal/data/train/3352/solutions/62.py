def find_longest(arr):
    for i in arr:
        if len(str(i)) == max((len(str(i)) for i in arr)):
            return i
