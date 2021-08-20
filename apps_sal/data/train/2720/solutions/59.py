def solution(digits):
    b = int(max((digits[a:a + 5] for a in range(len(digits) - 4))))
    return b
