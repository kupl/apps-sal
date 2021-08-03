def alternate_sort(l):
    l = sorted(l, key=abs)
    positives = [n for n in l if n >= 0]
    negatives = [n for n in l if n < 0]

    result = []
    while positives and negatives:
        result.append(negatives.pop(0))
        result.append(positives.pop(0))
    return result + positives + negatives
