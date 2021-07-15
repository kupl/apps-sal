def array_leaders(numbers):
    sum_right = 0
    result = []
    for num in reversed(numbers):
        if num > sum_right:
            result.append(num)
        sum_right += num
    return result[::-1]
