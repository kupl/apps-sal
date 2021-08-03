def solution(digits):
    result = -1
    for i in range(len(digits)):
        current = int(digits[i: i + 5])
        if current >= result:
            result = current
    return result
