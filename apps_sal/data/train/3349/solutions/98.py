def find_missing_number(sequence):
    if sequence == "":
        return 0
    try:
        sq = [int(x) for x in sequence.split()]
    except:
        return 1
    mini, maxi = min(sq), max(sq)
    for x in range(mini, maxi + 1):
        if x not in sq:
            return x
    return mini - 1
