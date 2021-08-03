def distinct(seq):
    newSeq, tmp = [], None

    for i in seq:
        if i != tmp and i not in newSeq:
            newSeq.append(i)
            tmp = i

    return newSeq
