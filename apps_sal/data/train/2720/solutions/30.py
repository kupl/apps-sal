def solution(digits):       
    k = []
    for i in range(len(digits)): k.append(int(digits[i:i+5]))
    return max(k)
