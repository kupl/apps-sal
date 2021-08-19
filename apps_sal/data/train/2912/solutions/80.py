def find_multiples(integer, limit):
    arr = []
    for i in range(integer, limit + 1):
        if i % integer == 0:
            arr.append(i)
    return arr
