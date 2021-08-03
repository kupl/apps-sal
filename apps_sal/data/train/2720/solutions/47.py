def solution(digits):
    cur = int(digits[:5])
    mx = cur
    for i in range(5, len(digits)):
        cur = (cur % 10000) * 10 + int(digits[i])
        if mx < cur:
            mx = cur
    return mx
