def example_sort(arr, example_arr):
    sorted_arr = []
    number_count = {}

    # Iterate through array and count number of items
    for n in arr:
        number_count[n] = number_count.get(n, 0) + 1

    # Iterate through example ordered array
    for n in example_arr:
        num_count = number_count.get(n, 0)
        for i in range(num_count):
            sorted_arr.append(n) # Push array count number of times in number_count

    return sorted_arr
