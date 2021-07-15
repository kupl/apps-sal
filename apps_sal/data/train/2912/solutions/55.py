def find_multiples(integer, limit):
    n = 1
    return_array = []
    while (integer*n <= limit):
        return_array.append(integer*n)
        n = n + 1
    return return_array
