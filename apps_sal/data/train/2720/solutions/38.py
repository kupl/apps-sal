def solution(digits):
    n = 0
    for i in range(len(digits)):
        if int(digits[i:i+5])>n:
            n = int(digits[i:i+5])
        
    return n
