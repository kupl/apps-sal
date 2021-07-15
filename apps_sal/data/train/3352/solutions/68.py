def find_longest(arr):
    m=len( str   (max(arr)))
    for x in arr:
        if len(str(x))==m:
            return x
