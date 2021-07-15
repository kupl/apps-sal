def simple_multiplication(number) :
    Temp = number % 2
    if Temp == 0:
        TempMul = number * 8
        return TempMul
    if Temp != 0:
        TempMul = number * 9
        return TempMul
