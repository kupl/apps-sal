def find_multiples(integer, limit):
    list = []
    i = 1
    while i <= (limit / integer):
        list.append(integer * i)
        i = i + 1
    return list
