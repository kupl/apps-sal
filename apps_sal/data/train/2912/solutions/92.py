def find_multiples(integer, limit):
    result = []
    for i in range((limit//integer)+1):
        result.append(integer*i)
        
    return result[1:]
