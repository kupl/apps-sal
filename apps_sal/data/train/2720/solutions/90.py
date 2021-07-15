def solution(digits):
    number = 0
    for i in range(len(digits)):
        num = int(digits[i:i+5])
        if num > number:
            number = num
    return number;
