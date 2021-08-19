def solution(digits):
    maxes = max([int(digits[j:j + 5]) for (j, k) in enumerate(digits)])
    return maxes
