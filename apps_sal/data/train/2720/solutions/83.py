def solution(digits):
    num, i = 0, 0
    while i < len(digits) - 4:
        if int(digits[i:i + 5]) > num:
            num = int(digits[i:i + 5])
        i += 1
    return num
