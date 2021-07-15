import numpy as np
from scipy.ndimage import generic_filter

def get_cell(cells):
    m, n = cells[4], sum(cells[:4]+cells[5:])
    return n==3 or (n==2 and m)

def crop_window(cells):
    r, c = tuple(cells.any(i).nonzero()[0] for i in (1,0))
    return cells[r[0]:r[-1]+1, c[0]:c[-1]+1].tolist() if r.size else [[]]
    
def get_generation(cells, gens):
    for i in range(gens):
        cells = np.pad(cells, 1, 'constant')
        cells = generic_filter(cells, get_cell, size=(3,3), mode='constant')
        cells = crop_window(cells)
    return cells
