def solution(digits):
    best = 0
    for i in range(len(digits) - 4):
        n = int(digits[i:i + 5])
        if n > best:
            best = n
    return best
