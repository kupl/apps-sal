def largest_rect(histogram):
    if not histogram:
        return 0

    maxi = 0
    pile = []

    for elt in histogram:
        coeff = 0
        while(pile and elt < pile[-1][0]):
            top1, top2 = pile.pop()
            coeff += top2
            score = top1 * coeff
            maxi = max(maxi, score)

        pile.append([elt, coeff + 1])

    coeff = 0
    while(pile):
        top1, top2 = pile.pop()
        coeff += top2
        score = top1 * coeff
        maxi = max(maxi, score)

    return maxi
