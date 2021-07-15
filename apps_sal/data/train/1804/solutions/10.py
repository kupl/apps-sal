def recoverSecret(triplets):
    # Initialize the answer to the letters we're given in the triplets (use set() to drop duplicates)
    answer = list(set([item for sublist in triplets for item in sublist]))
    # Convert the triplets into sets of pairs, to more easily do comparisons
    clues = []
    for t in triplets:             # copy remaining triplets as pairs
        clues.append([t[0], t[1]])
        clues.append([t[1], t[2]])

    # Loop through the clue pairs, swapping (sorting) letters that are out of order.
    # Once we've made no more swaps, we know we are done.
    while True:
        changed = False
        for pair in clues:
            left = answer.index(pair[0])
            right = answer.index(pair[1])
            if left > right:     # These letters are out-of-order, so swap them
                answer[left], answer[right] = answer[right], answer[left]
                changed = True
        if not changed:
            break
    return "".join(answer)
