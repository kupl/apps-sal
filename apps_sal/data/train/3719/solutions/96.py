def starting_mark(h):
    return round(starting_mark.k*h+starting_mark.d, 2)
starting_mark.eg = [(1.52,9.45),(1.83,10.67)]
starting_mark.k = (starting_mark.eg[1][1]-starting_mark.eg[0][1])/(starting_mark.eg[1][0]-starting_mark.eg[0][0])
starting_mark.d = starting_mark.eg[0][1]-starting_mark.k*starting_mark.eg[0][0]
