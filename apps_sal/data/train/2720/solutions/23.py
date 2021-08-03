def solution(digits):
    result = digits[:6]
    for i in range(len(digits)):
        s = digits[i:i + 5]
        if len(s) < 5:
            break
        if result < s:
            result = s
    return int(result)
