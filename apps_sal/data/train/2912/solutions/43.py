def find_multiples(integer, limit):
    result_list = [integer]
    counting = integer
    while counting < limit:
        counting += integer
        if counting > limit:
            break
        else:
            result_list.append(counting)
    return result_list
