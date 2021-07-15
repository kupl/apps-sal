def solution(digits):
    v = [digits[i:i+5] for i in range(len(digits)-4)]
    v.sort()
    return int(v[-1])
