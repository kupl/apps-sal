def solution(digits):
    i, k = 0, []
    while i < len(digits):
        k.append(int(digits[i:i + 5]))
        i += 1
    return max(k)
