def sum_digits(number):
    
    if number<0:
        number = number * -1
        
    number=str(number)
    
    sum=0
    
    for i in number:
        
        sum+=int(i)
        
    return sum

