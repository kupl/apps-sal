def distinct(seq):
    sum = []
    for i in seq:
        if i not in sum:
            sum.append(i)
    return sum
