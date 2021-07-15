def strong_num(number):
    
    sum = 0
    for i in map(int,str(number)):
        temp = 1
        for j in range(i,1,-1):
            temp *= j
        sum += temp
    print(number,sum)
    if number == sum:
        return "STRONG!!!!"
    return "Not Strong !!"
