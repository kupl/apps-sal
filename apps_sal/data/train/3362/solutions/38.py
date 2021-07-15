def sum_mix(arr):
    tam = len(arr) #Tamanho do array
    num = 0
    soma = 0
    
    for num in range(tam): #Separar cada elementro do array
        y = int(arr[num])
        num = num + 1
        soma += y #soma o último valor com a variável atual

    return soma
    #your code here

