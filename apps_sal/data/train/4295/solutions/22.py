def balanced_num(num):
    digits = [int(digit) for digit in str(num)]
    half = (len(digits) - 1) // 2
    left_sum, right_sum = sum(digits[:half]), sum(digits[-half:])
    return ('' if num < 100 or left_sum == right_sum else 'Not ') + 'Balanced'
