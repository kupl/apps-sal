def find_multiples(integer, limit):
    lst = []
    count = 1
    while integer * count <= limit:
        var = integer * count
        lst.append(var)
        count += 1
    return lst

