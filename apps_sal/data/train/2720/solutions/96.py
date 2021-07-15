def solution(digits):
    max_num = 0
    for i in range(len(digits)-4):
        curr_num = int(digits[i:i+5])
        if curr_num > max_num:
            max_num = curr_num
    return max_num
