def solution(digits):
    max = 0
    for i in range(0, len(digits)):
        n = int(digits[i:i + 5])
        if n > max:
            max = n

    return max
