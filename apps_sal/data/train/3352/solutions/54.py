def find_longest(arr):
    longest = 0
    number = 0
    for i in arr:
        if len(str(i)) > longest:
            longest = len(str(i))
            number = i
    return number
