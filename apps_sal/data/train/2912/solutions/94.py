def find_multiples(integer, limit):
    result = []
    number = 1
    temp = integer * number
    while temp <= limit:
        result.append(temp)
        number += 1
        temp = integer * number
    return result

