def isDigit(string):
    try:
        resultado = float(string)  # puedes convertir string a float? si? entonces True
        return True
    except ValueError:  # No puedes? entonces devuelve falso
        return False
