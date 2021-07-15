def solution(digits):
    biggest = 0
    for x in range(len(digits)-4):
        num = int(digits[x]+digits[x+1]+digits[x+2]+digits[x+3]+digits[x+4])
        if num > biggest:
            biggest = num
    return biggest
