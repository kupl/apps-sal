def isDigit(string):
    potential_digit = string.strip()
    try:
        digit = float(potential_digit)
    except:
        return False
    else:
        return True
