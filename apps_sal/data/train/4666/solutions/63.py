def array_plus_array(arr1, arr2):
    Liste = list()
    for index in range(len(arr1)):
        sum1 = arr1[index] + arr2[index]
        Liste.append(sum1)
    return sum(Liste)
