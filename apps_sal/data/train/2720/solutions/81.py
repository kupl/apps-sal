def solution(digits):
    x = []
    for i in range(0, len(digits)):
        x.append(int(digits[i:i + 5]))
    return max(x)
