def isDigit(string):
    try:
        resultado = float(string)
        return True
    except ValueError:
        return False
