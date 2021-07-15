def solution(digits):
    ans = 0
    for i in range (0, len(digits)):
        if int(digits[i:i+5]) > ans:
            ans = int(digits[i:i+5])
    return ans
