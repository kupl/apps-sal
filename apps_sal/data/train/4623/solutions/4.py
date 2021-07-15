import numpy as np
def make_2d_list(head,row,col):
    x = np.arange(head, head+row*col)
    x = x.reshape(row, col)
    return x.tolist()
