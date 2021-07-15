def is_divide_by(number, a, b):
    if number % a == 0 and number % b ==0:
        return True
    elif number % a != 0 or number % b != 0: 
        return False
    else:
        return None

