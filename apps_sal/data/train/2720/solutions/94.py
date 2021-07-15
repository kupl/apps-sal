def solution(digits):
    max = 0
    seq = 0
    for d in range(0,len(digits)):
        seq = int(digits[d:d+5])
        if seq > max:
            max = seq
    return max
