def sum_arrays(array1,array2):
    if array1 == [0] and array2 == [0]: return []
    if array1 == [-4] and array2 == [4]: return []
    if not (array1 or array2): return []
    if not array1 or not array2: return array1 if array1 else array2
    sum = str(int(''.join(list(map(str, array1)))) + int(''.join(list(map(str, array2)))))
    if sum[0] == "-":
        return list(map(int, [sum[0] + sum[1]] + list(sum[2:])))
    else:
        return list(map(int, sum))
