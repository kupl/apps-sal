def paint_letterboxes(start, finish):
    frequencies = [0]*10
    for i in range(start, finish+1):
        for d in str(i):
            frequencies[int(d)] += 1
    return frequencies
