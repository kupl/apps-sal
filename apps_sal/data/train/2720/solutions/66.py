def solution(digits):
    biggest = int(digits[0:5])
    for i in range(0,int(len(digits))-4):
        if biggest<int(digits[i:i+5]):
            biggest = int(digits[i:i+5])
    return biggest
