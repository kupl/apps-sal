def solution(digits):
    x = 0
    m = 5
    i = 0
    for i in range(len(digits)):
        if int(digits[i:i+5]) > x:
            x = int(digits[i:i+5])
            i += 1
    else:
        i += 1
    
    return x
