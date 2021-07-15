def strong_num(number):
    def factorial(n):
        if n == 0:
            return 1
        else:
            output = 1
            for i in range(1,n+1):
                output *= i
            return output
    suma = 0
    for num in str(number):
        suma += factorial(int(num))
    if suma == number:
        return "STRONG!!!!"
    else:
        return "Not Strong !!"
