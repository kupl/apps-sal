sort_by_value_and_index = lambda arr: [elem for key, original_index, elem in sorted(((i * elem, i, elem) for i, elem in enumerate(arr, 1)))]
