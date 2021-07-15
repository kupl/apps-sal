def find_multiples(integer, limit):
    arr = []
    count = integer
    while count <= limit:
        arr.append(count)
        count += integer
    return arr
