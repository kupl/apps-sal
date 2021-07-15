def twos_difference(lst): 
    my_pairs = []
    for i in range(0, len(lst)):
        for j in range (0, len(lst)):
            if lst[j] - lst[i] == 2:
                my_pairs.append([lst[j],lst[i]])
    diffs = []
    for pair in my_pairs:
        pair.sort()
        diffs.append(tuple(pair))
        
    diffs.sort()
    return diffs
