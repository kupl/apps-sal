import numpy as np
def symmetric_point(p, q):
    
    d = list(np.add(q,np.subtract(q,p)))
    
    return d
