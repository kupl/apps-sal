def symmetric_point(p, q):

    difference = []

    zip_object = zip(p, q)
    for p, q in zip_object:
        difference.append(2 * q - p)

    return(difference)
