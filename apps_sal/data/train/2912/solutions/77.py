def find_multiples(integer, limit):
    count = int(limit / integer)
    result = []

    for i in range(count):
        result.append(integer * (i + 1))

    return result
