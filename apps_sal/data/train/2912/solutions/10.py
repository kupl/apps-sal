def find_multiples(integer, limit):
    result = []
    i = integer
    for i in range(limit+1):
        if ((i % integer == 0) and (i != 0)):
            result.append(i)
    return result  
