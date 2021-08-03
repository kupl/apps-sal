def solution(digits):
    cc = []
    for i in range(len(digits)):
        cc.append(digits[i:i + 5])
    return int(max(cc))
