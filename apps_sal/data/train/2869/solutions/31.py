def distinct(seq):
    arr = [seq[0]]
    a = seq[0]
    for x in range(1, len(seq)):
        if not seq[x] in arr:
            arr.append(seq[x])
    return arr
