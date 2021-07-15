def sum_triangular_numbers(n):
    
    if n > 0 :

        listado_numeros = []

        while len(listado_numeros) < n :# genera lista con los numeros hasta N
            for i in range (1,n+1):
                listado_numeros.append(i)
        
        for i in listado_numeros[1:]:
            listado_numeros[i-1] = i + listado_numeros[i-2]

        return (sum(listado_numeros))

    else:

        return (0)
