def make_2d_list(head,row,col):
    return [[head + c + r*col for c in range(col)] for r in range(row)]
