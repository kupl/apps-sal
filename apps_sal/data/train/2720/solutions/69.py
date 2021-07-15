def solution(digits):
    
    all = []
    for x in range(len(digits)):
        all.append(int(digits[x:x+5]))
    
    return max(all)
