def solution(digits):
    max_num = 0
    for index in range(len(digits) - 4):
        num = int(digits[index:index + 5])
        if num > max_num:
            max_num = num
    print(max_num)
    return max_num
