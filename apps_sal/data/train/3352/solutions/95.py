def find_longest(arr):
    most_digits = arr[0]  # value of index of given array starts with the first entry
    for i in arr:
        if len(str(i)) > len(str(most_digits)):  # if next entry has larger len(str())
            most_digits = i  # array index is replaced with new index where number with more digits appears
    return most_digits
