def two_highest(arg1):
    zrobmyset = set(arg1)
    listabezdupl = list(zrobmyset)
    listabezdupl.sort()
    listabezdupl.reverse()
    return listabezdupl[:2]
