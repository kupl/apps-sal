def invite_more_women(arr):
    contador_hombres = 0
    contador_mujeres = 0
    for elemento in arr:
        if elemento == -1:
            contador_mujeres = contador_mujeres + 1
        if elemento == 1:
            contador_hombres = contador_hombres + 1
    if arr == []:
        return False
    elif contador_hombres <= contador_mujeres:
        return False
    else:
        return True
