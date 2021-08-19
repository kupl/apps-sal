def solution(digits):
    ans = None
    for i in range(0, len(digits)):
        if ans is None:
            ans = int(digits[i:i + 5])
        elif int(digits[i:i + 5]) > ans:
            ans = int(digits[i:i + 5])
    return ans
