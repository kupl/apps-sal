def sum_arrays(array1,array2):
    number1 = 0
    number2 = 0
    b1 = False
    b2 = False
    if len(array1) == 0:
        return array2
    if len(array2) == 0:
        return array1
    if array1[0] < 0:
        array1[0] *= -1
        b1 = True
    if array2[0] < 0:
        array2[0] *= -1
        b2 = True
    for i in array1:
        number1 = number1 * 10 + i
    for i in array2:
        number2 = number2 * 10 + i
    if b1:
        number1 *= -1
    if b2:
        number2 *= -1
    number = number1 + number2
    array = []
    if number == 0:
        return []
    if number < 0:
        b = True
        number *= -1
    else:
        b = False
    number = str(number)
    for i in range(len(number)):
        array.append(int(number[i]))
    if b:
        array[0] *= -1
        return array
    return array
