def find_longest(arr):
    most_digits = arr[0]
    for i in arr:
        if len(str(i)) > len(str(most_digits)):
            most_digits = i
    return most_digits
