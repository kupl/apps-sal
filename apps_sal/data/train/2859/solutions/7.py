def largest_sum(arr):
    best_sum = 0
    current_sum = 0
    for item in arr:
        current_sum += item
        if current_sum < 0:
            current_sum = 0
        else:
            if current_sum > best_sum:
                best_sum = current_sum
    return best_sum
