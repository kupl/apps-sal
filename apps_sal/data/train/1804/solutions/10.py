def recoverSecret(triplets):
    answer = list(set([item for sublist in triplets for item in sublist]))
    clues = []
    for t in triplets:
        clues.append([t[0], t[1]])
        clues.append([t[1], t[2]])

    while True:
        changed = False
        for pair in clues:
            left = answer.index(pair[0])
            right = answer.index(pair[1])
            if left > right:
                answer[left], answer[right] = answer[right], answer[left]
                changed = True
        if not changed:
            break
    return "".join(answer)
