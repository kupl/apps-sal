def strong_num(number):
    Digits = list(map(int,list(str(number))))
    SumFactorial = 0
    for i in Digits:
        Factorial = 1
        for x in range(1, i+1):
            Factorial *= x
        SumFactorial += Factorial
    if SumFactorial == number:
        return "STRONG!!!!"
    else:
        print(number)
        return "Not Strong !!"

