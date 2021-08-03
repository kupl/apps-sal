def solution(digits):
    maxNum = 0
    for i in range(len(digits) - 4):
        curNum = int(digits[i:i + 5])
        if curNum > maxNum:
            maxNum = curNum
    return maxNum
