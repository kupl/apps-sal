def solution(digits):
    
    l = []
    
    for i in range(len(str(digits))-4):
        total = int(digits[i:i+5])
        l.append(total)
    return(max(l))
    

