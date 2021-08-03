from collections import Counter


def distinct(seq):
    listt = list()
    seq = Counter(seq)
    for i in list(seq.items()):
        listt.append(i[0])

    return listt
