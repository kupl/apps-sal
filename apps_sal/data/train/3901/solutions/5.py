def check_digit(number, index1, index2, digit):
    nums = str(number)
    if index2 < index1:
        index2, index1 = index1, index2

    return str(digit) in nums[index1:index2 + 1]
