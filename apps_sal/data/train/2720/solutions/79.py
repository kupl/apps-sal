def solution(digits):
    return max([int(digits[loop] + digits[loop + 1] + digits[loop + 2] + digits[loop + 3] + digits[loop + 4]) for loop in range(len(digits) - 4)])
