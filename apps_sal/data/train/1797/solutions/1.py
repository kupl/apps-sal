# Based on http://www.codewars.com/kata/reviews/53d0337689316446e6000035/groups/5406bde018340bce700006c4
# We don't need to recalculate next_hamms on each iteration.
# Recalculating only the changed values results in some 35% performance improvement.
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
