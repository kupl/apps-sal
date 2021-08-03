def find_multiples(integer, limit):
    arr = [integer]
    # print(range(int(limit//integer)-1))
    for i in range(int(limit // integer) - 1):
        if arr[-1] < limit:
            arr.append(2 * integer + integer * i)
    return arr
