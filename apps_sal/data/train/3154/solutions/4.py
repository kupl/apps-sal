def color_2_grey(colors):
    return [[[round(sum(p)/3) for i in p] for p in r] for r in colors]
