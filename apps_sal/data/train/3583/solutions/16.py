def binary_array_to_number(arr):
    strng = ' '
    for nr in arr:
        strng = strng + str(nr)
    return int(strng, 2)
