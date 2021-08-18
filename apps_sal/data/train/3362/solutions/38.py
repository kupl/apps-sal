def sum_mix(arr):
    tam = len(arr)
    num = 0
    soma = 0

    for num in range(tam):
        y = int(arr[num])
        num = num + 1
        soma += y

    return soma
