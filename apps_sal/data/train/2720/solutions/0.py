def solution(digits):
    numlist = [int(digits[i:i+5]) for i in range(0,len(digits)-4)]
    return max(numlist)
