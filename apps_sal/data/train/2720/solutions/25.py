def solution(digits):
    x = str(digits)
    empty = []
    for i in range(0,len(x)):
        empty.append(int(x[i:i+5]))
        
    return max(empty)
