def find_multiples(integer, limit):
    res = []
    multiple = 0
    flag = 1
    while flag <= (limit // integer):
        multiple = integer * flag
        flag += 1
        res.append(multiple)
    return res
