def array_plus_array(arr1,arr2):
    soma = 0
    for i in range(len(arr1)):
        soma += arr1[i]
    for i in range(len(arr2)):
        soma += arr2[i]
    return soma

