def complete_series(seq): 
    from collections import Counter
    if Counter(seq).most_common()[0][1] > 1:
        return [0]
    return [i for i in range(max(seq)+1)]
