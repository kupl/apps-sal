def reverse(right):
    xs = []
    for y in right:
        ys = [y]
        for x in xs:
            ys.append(x - ys[-1])
        xs = ys
    return xs[::-1]
