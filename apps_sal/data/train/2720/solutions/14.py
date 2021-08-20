def solution(digits):
    return max((int(digits[i - 5:i]) for (i, _) in enumerate(digits, 5)))
