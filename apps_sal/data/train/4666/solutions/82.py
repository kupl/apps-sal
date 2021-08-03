def array_plus_array(arr1, arr2):
    resultado = 0
    for i in range(len(arr1)):
        resultado = resultado + arr1[i]
    for i in range(len(arr2)):
        resultado = resultado + arr2[i]
    return resultado
