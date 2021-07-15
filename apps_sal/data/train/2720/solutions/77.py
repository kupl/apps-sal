def solution(digits):
    lst = [digits[i:i+5] for i in range(0, len(digits))]
    return int(max(lst))

