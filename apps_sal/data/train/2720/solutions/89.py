def solution(digits):
    step_index = 0
    index = 0
    step_sum = ''
    max_sum = '0'
    while step_index + 5 != len(digits) + 1:
        while index < step_index + 5:
            step_sum += digits[index]
            index = index + 1
        step_index = step_index + 1
        index = index - 5 + 1
        if int(step_sum) > int(max_sum):
            max_sum = step_sum
        step_sum = ''
    return int(max_sum)
