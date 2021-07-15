def solution(digits):
    largest = ''
    for i in range(len(digits) - 4):
        if digits[i:i+5] > largest:
            largest = digits[i:i+5]
    return int(largest)
