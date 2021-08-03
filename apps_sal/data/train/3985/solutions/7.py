def find_even_index(arr):
    left_sum, right_sum = 0, sum(arr)

    for i, n in enumerate(arr):
        right_sum -= n
        if left_sum == right_sum:
            return i
        left_sum += n

    return -1
