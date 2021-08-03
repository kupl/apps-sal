def solution(digits):
    number = 0
    max = 0
    for i in range(len(digits) - 4):
        number = digits[i:i + 5]
        number = int(number)
        if number > max:
            max = number
    return max
