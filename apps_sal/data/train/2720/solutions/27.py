def solution(digits):
    return max([int(digits[item:item+5]) for item in range(len(digits)-4)])
