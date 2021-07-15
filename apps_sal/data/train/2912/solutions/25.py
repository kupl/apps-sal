def find_multiples(integer, limit):
    result = []
    num = 1
    while integer * num <= limit:
        result.append(integer * num)
        num += 1
    return result
