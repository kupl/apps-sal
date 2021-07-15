from itertools import count

def make_2d_list(head,row,col):
    c = count(0)
    return [[ head+next(c) for _ in range(col)] for _ in range(row)]
