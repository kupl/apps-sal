def find_longest(arr):
    convert = 0
    for i in arr:
        if len(str(i)) == len(str(max(arr))):
            convert = i
            break
    return convert
