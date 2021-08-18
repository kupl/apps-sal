def find_longest(arr):
    longest_item = 0
    i = 0
    while i < len(arr):
        if len(str(longest_item)) < len(str(arr[i])):
            longest_item = arr[i]
            i += 1
        else:
            i += 1
    return longest_item
