dict = {
    True: 1,
    False: 2
}


def logical_calc(array, op):
    print(array, op)
    arrn = []
    length = len(array)
    for x in array:
        arrn.append(dict[x])
    if op == "XOR":
        if sum(arrn) == 1:
            return True
        elif sum(arrn) == 2:
            return False
        else:
            i = 0
            x = array[0]
            while i < len(array) - 1:
                x = x == array[i + 1]
                i += 1
            if x:
                return False
            else:
                return True
    elif sum(arrn) == length and op == "AND":
        return True
    elif array.count(False) == length:
        return False
    elif (sum(arrn) != length or sum(arrn) != length * 2) and op == "OR":
        return True
    else:
        return False
