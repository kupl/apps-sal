def find_multiples(integer, limit):
    arr = [integer]
    x = integer
    if limit // integer:
        while x + integer <= limit:
            x += integer
            arr.append(x)
    return arr
