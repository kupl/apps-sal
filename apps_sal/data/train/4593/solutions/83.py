def merge_arrays(arr1, arr2):
    if arr1 == [] and arr2 == []:
        return []
    salida = arr1 + arr2
    return sorted(set(salida))
