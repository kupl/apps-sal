import numpy as np

def sum_of_threes(n):
    s=np.base_repr(n,3)
    if '2' in s: return 'Impossible'
    return '+'.join(['3^{}'.format(i) for i,d in enumerate(s[::-1]) if d=='1'][::-1])

