def squares_needed(grains):
    # condition: when does the recursion stop?
    if grains < 1 :
        return 0
    # what changes in each iteration? The grains are halved
    grains = grains//2
    # since the final iteration returns 0, you add 1 to each result
    print(grains)
    return 1 + squares_needed(grains)

