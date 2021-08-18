def is_sorted_and_how(arr):
    type_arr = set()

    prev = arr[0]

    for item in arr[1:]:
        if item > prev:
            type_arr.add('asc')

        elif item < prev:
            type_arr.add('desc')
        prev = item

    if len(type_arr) != 1:
        return 'no'

    result = type_arr.pop()
    return 'yes, ascending' if result == 'asc' else 'yes, descending'
