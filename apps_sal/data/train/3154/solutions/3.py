def color_2_grey(a):
    return [[[round(sum(y) / 3)] * 3 for y in x] for x in a]
