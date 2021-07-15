def find_multiples(integer, limit):
    aha = []
    x = 0
    while x <= limit:
        x = x + integer
        if x <= limit:
            aha.append(x)
    return aha

