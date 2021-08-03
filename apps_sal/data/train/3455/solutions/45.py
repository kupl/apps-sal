def disarium_number(number):
    Digits = list(map(int, list(str(number))))
    SumDigitsPow = 0
    for i in range(len(Digits)):
        SumDigitsPow += pow(Digits[i], i + 1)
    if SumDigitsPow == number:
        return "Disarium !!"
    else:
        return "Not !!"
