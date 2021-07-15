def solution(digits):
    return max([int(digits[start:start+5]) for start in range(len(digits))])

