def solution(digits):
    number = 0
    digits = str(digits)
    for i in range(len(digits)):
        slice = digits[i:i + 5]
        if  int(slice) > number: number = int(slice) 
    return number

