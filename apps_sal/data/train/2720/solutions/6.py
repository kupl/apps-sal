def solution(digits):
    return int(max(''.join(digits[n:n + 5]) for n in range(len(digits) - 4)))

