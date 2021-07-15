def is_divide_by(number, a, b):
    rezultat = number % a or number % b
    if rezultat == 0:
        return True
    else:
        return False
