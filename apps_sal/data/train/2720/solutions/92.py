def solution(digits):
    if len(digits) < 5:
        return int(digits)
    i = 0
    ans = 0
    for j in range(len(digits)):
        while j - i + 1 > 5:
            i += 1
        num = int(digits[i:j + 1])
        if num > ans:
            ans = num
    return ans
