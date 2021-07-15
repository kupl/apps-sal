def solution(digits):
    mx = 0
    for i in range(len(digits) - 4):
        n = int(digits[i:i + 5])
        if n > mx:
            mx = n
    return mx
