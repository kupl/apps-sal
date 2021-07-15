def solution(digits):
    maxima = 0
    for i in range(len(digits)):
        if int(digits[i:i+5]) > maxima:
            maxima = int(digits[i:i+5])
    return maxima

