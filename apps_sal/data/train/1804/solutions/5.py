def recoverSecret(triplets):
    'triplets is a list of triplets from the secrent string. Return the string.'
    res = ''
    while triplets != []:
        non_firsts = [num for t in triplets for num in t[1:]]
        firsts = [t[0] for t in triplets]
        for f in firsts:
            if f not in non_firsts:
                res += f
                for t in triplets:
                    if t[0] == f:
                        t.pop(0)
                break
        triplets = [t for t in triplets if t != []]
    return res
