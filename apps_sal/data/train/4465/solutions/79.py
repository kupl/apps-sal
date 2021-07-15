def super_size(n):
    if len(str(n)) > 1:
        array_numbers = map(int, str(n))
        sorted_arrays = sorted(array_numbers, reverse=True)
        strings = [str(sorted_array) for sorted_array in sorted_arrays]
        a_string = "".join(strings)
        result = int(a_string)
        return result
    else:
        return n
