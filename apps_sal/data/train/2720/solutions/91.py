def solution(digits):
    num = 0
    for x in range(0, len(digits)-1):
        if int(digits[x:x+5]) > int(num):
            num = digits[x:x+5] 
    return(int(num))
