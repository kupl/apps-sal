def find_multiples(integer, limit):
    result = 0
    arr = []
    for i in range(int(limit / integer)):
        result = result + integer
        arr.append(result)
    return arr

