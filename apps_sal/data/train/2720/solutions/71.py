def solution(digits):
    record=0
    for i in range(0,len(digits)-4):
        current = int(digits[i:i+5])
        #print(current)
        if current > record:
            record = current
    return record
