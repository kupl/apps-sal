def sum_arrangements(num):
    num = str(num)
    n = 1
    number = len(num)
    for i in range(1,number):
        n *= i
    return int('1'*number)*sum(int(i) for i in num)*n
    
    

