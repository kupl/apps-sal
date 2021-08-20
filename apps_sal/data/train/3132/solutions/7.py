def alternate_sort(l):
    negatives = sorted((n for n in l if n < 0), key=abs)
    positives = sorted((n for n in l if n > -1))
    return [lst[i] for i in range(max(len(negatives), len(positives))) for lst in (negatives, positives) if i < len(lst)]
