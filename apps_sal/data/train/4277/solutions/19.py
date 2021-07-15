def difference_in_ages(ages):
    lista_noua = []
    lista_noua.append(min(ages))
    lista_noua.append(max(ages))
    diferenta = lista_noua[1] - lista_noua[0]
    lista_noua.append(diferenta)
    tupled = tuple(lista_noua)
    return tupled

