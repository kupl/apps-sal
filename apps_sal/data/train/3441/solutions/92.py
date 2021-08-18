
def get_average(marks):
    suma = 0
    for x in marks:
        suma = suma + x
    return (suma // len(marks))
