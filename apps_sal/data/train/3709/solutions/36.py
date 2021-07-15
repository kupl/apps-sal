def simple_multiplication(number) :
    print(number)
    if number % 2 == 0:
        simple_multiplication = number * 8
    elif number % 2 == 1:
        simple_multiplication = number * 9
    return(simple_multiplication)
