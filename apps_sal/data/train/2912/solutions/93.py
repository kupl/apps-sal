def find_multiples(integer, limit):
    count = 1
    res = []
    while True:
        somme = integer * count
        if somme > limit:
            break
        else:
            res.append(somme)
            count += 1
    return res
