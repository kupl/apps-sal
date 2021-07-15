def find_longest(arr):
    longest = 0
    result = 0
    for item in arr:
        if len(str(item)) > longest:
            longest = len(str(item))
            result = item
            
    return result
