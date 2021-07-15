def power_mod(base, exponent, modulus):
    if base is 0: return 0
    if exponent is 0: return 0
    base = base % modulus
    result = 1
    while (exponent > 0):
        if (exponent % 2 == 1):
           result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result
