def derive(coefficient, exponent):
    new_coefficient = coefficient * exponent
    new_exponent = exponent - 1
    ans = str(new_coefficient) + "x^" + str(new_exponent)
    return ans
