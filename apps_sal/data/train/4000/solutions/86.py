def strong_num(number):
    
    def factorial(n):
        factorial = 1
        for x in range(1,int(n)+1):
            factorial = factorial*x
        return factorial
        
        
        
    s = 0
    for digit in str(number):
        s+=factorial(digit)
    
    if s==number:
        return "STRONG!!!!"
    else:
        return "Not Strong !!"
