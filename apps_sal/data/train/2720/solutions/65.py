def solution(digits):
    num = [digits[i:i+5] for i in range(len(digits)-4)]
    num.sort()
    return int(num[-1])

