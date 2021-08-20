def problem(a):
    if isinstance(a, (int, float)):
        print(a)
        resultado = a * 50 + 6
        print(resultado)
        return resultado
    else:
        return 'Error'
