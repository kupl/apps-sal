def find(num):
    result = []
    num = list(range(1,num+1))
    for zahl in num:
        if (zahl%3 == 0) or (zahl%5 == 0):
            result.append(zahl) 
    return sum(result)
