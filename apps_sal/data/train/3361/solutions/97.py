def sum_of_minimums(numbers):
    minimum_arr = []
    for arr in numbers:
        minimum_arr.append(min(arr))
    return sum(minimum_arr)
