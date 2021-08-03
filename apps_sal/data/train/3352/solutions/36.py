def find_longest(arr):
    realnum = 0
    for item in arr:
        if len(str(item)) > len(str(realnum)):
            realnum = item
    return realnum
