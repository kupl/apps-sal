def derive(coefficient, exponent):
    # your code here
    answer = coefficient * exponent
    exponent -= 1

    return "{}x^{}".format(answer, exponent)
