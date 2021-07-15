def solution(digits):
    maxdi = 0
    for i in range(len(digits)-4):
        each5 = int(digits[i:i+5])
        if each5 > maxdi:
            maxdi = each5
    return maxdi
