def hamming(n):
    bases = [2, 3, 5]
    expos = [0, 0, 0]
    hamms = [1]
    next_hamms = [2, 3, 5]
    for _ in range(1, n):
        next_hamm = min(next_hamms)
        hamms.append(next_hamm)
        for i in range(3):
            if next_hamms[i] == next_hamm:
                expos[i] += 1
                next_hamms[i] = bases[i] * hamms[expos[i]]
    return hamms[-1]
