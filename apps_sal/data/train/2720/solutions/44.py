def solution(digits):
    digits = str(digits)
    x = [int(digits[i:i + 5]) for i in range(len(digits) - 4)]
    return max(x)
