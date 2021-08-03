def count_by(x, n):
    counter = 0
    multiples = []
    i = 1
    while counter < n:
        if i % x == 0:
            counter += 1
            multiples.append(i)
        i += 1

    return multiples
