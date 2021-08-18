def example_sort(arr, example_arr):
    sorted_arr = []
    number_count = {}

    for n in arr:
        number_count[n] = number_count.get(n, 0) + 1

    for n in example_arr:
        num_count = number_count.get(n, 0)
        for i in range(num_count):
            sorted_arr.append(n)

    return sorted_arr
