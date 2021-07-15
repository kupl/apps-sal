def sort_nested_list(A):
    sort_nested_list.numbers = []
    def collect_numbers(lista):
        if len(lista) == 0:
            return lista
        if len(lista) > 1:
            for i in lista:
                try:
                    for e in i:
                        for q in e:
                            sort_nested_list.numbers.append(q)
                except:
                    return sorted(lista)
            return lista
        else:
            return [collect_numbers(lista[0])]

    def place_numbers(lista):
        if len(lista) == 0:
            return lista
        if len(lista) > 1:
            for i in lista:
                try:
                    for e in i:
                        for index, element in enumerate(e):
                            e[index] = sort_nested_list.numbers.pop(0)
                except:
                    return sorted(lista)
            return lista
        else:
            return [place_numbers(lista[0])]

    collect_numbers(A)
    sort_nested_list.numbers.sort()

    return place_numbers(A)
