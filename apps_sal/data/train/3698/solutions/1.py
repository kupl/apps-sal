def tiy_fizz_buzz(strin):
    strin = list(strin)
    for i, char in enumerate(strin):
        if   char in "AEIOU"                 : strin[i] = "Iron Yard"
        elif char in "aeiou"                 : strin[i] = "Yard"
        elif char in "QWRTYPSDFGHJKLZXCVBNM" : strin[i] = "Iron"
    return ''.join(strin)
