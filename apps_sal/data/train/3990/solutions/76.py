def derive(coefficient, exponent):
    answer = coefficient * exponent
    exponent -= 1

    return "{}x^{}".format(answer, exponent)
