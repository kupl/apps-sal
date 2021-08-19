
def is_divide_by(number, a, b):
    # Use modulus to check for perfect division
    if (number % a == 0 and number % b == 0) == True:
        return True
    else:
        return False


print(is_divide_by(-12, 2, -6))   # good luck
