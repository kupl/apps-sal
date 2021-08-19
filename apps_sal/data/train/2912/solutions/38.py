def find_multiples(integer, limit):
    multiple_list = []
    for num in range(limit + 1):
        if num == 0:
            pass
        elif num % integer == 0:
            multiple_list.append(num)
        else:
            pass
    return multiple_list
