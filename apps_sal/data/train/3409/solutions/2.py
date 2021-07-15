def fish(shoal, size = 1, protein_earned = 0):
    fishes = [int(fish) for fish in shoal if fish != '0']
    grow = True
    while grow:
        edible_fishes = list(filter(lambda x: x <= size, fishes))
        ate_protein = sum(edible_fishes)
        protein_earned += ate_protein
        if protein_earned >= protein_to_grow(size):
            size += 1
            fishes = [fish for fish in fishes if fish not in edible_fishes]
        else:
            grow = False
    return size

def protein_to_grow(actual_size):
    protein_to_accumulate = 0
    while actual_size > 0:
        protein_to_accumulate += actual_size * 4
        actual_size -= 1
    return protein_to_accumulate
