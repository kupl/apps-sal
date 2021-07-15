def solution(digits):
    return int(max(digits[a:a + 5] for a in range(len(digits) - 4)))
