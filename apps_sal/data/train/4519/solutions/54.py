def max_number(n):
    arrayTest = [1,3,2]
    array = list(str(n))
    array.sort(reverse=True)
    array1 = [str(array) for array in array]
    array2 = "".join(array1)
    array3 = int(array2)
    return array3
