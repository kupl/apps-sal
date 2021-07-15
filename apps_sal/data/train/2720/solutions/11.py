def solution(digits):
    a = []
    for i in range(len(digits)-4):
        a.append(give5LengthNumber(digits[i:]))
    return(int(max(a)))
    
def give5LengthNumber(num):
    return num[0:5]
