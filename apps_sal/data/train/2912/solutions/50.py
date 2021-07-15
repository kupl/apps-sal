def find_multiples(integer, limit):
    list = [integer]
    count = 2
    while integer * count <= limit:
        list.append(integer * count)
        count += 1
    return list
