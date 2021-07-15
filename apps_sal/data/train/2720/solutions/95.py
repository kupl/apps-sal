def solution(digits):
    numlist = [int(digits[i:i+5]) for i in range(len(digits))]
    return max(numlist)
