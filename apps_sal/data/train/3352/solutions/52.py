def find_longest(arr):
    convert = []
    for num in arr:
        convert.append(str(num))
    return int(sorted(convert, key=len, reverse=True)[0])
