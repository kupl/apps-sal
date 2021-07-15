# truncate name as array.
# si es menor o igual a 2 retorna el nombre como es.


def who_is_paying(name):
    if len(name) > 2:
        return [name, name[0:2]]
    else:
        return [name[0:len(name)]]
    

