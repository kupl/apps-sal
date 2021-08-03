def min_sum(arr):
    sum = 0
    sorted_arr = sorted(arr)
    front_i = 0
    back_i = len(arr) - 1

    while front_i < back_i:
        sum += sorted_arr[front_i] * sorted_arr[back_i]
        front_i += 1
        back_i -= 1
    return sum
