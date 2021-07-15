def strong_num(number):
    
    def factorial(n):
        if n < 2:
            return 1
        else:
            return n * factorial(n-1)
    
    if sum([factorial(int(i)) for i in str(number)]) == number:
        return 'STRONG!!!!'
    else:
        return 'Not Strong !!'
