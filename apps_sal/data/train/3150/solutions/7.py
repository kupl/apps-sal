def binary_cleaner(seq): 
    b = []
    x = []
    for i in range(len(seq)):
        if seq[i] < 2:
            b.append(seq[i])
        elif seq[i] > 1:
            x.append(i)
    return (b, x)
