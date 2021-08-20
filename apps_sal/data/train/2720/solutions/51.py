def solution(digits):
    h_seq = 0
    for i in range(0, len(digits) - 4):
        if int(digits[i:i + 5]) > h_seq:
            h_seq = int(digits[i:i + 5])
    return h_seq
