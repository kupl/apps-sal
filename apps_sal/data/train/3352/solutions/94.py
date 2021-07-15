def find_longest(arr):
    m= max(len(str(n)) for n in arr)
    for x in arr:
        if len(str(x))==m:
            return x
