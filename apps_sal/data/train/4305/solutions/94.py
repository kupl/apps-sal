def order_weight(strng):
    splitted = strng.split()
    solution = ''
    list = []
    for item in splitted:
        weight = 0
        for digit in item:
            weight += int(digit)
            arr = [weight, item]
        list.append(arr)
    list.sort()
    for item in list:
        solution += ' ' + item[1]
    return solution[1:]
