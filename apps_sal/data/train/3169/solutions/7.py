from collections import deque
from itertools import islice, groupby

def odd_penta_fib():
    q = deque([0, 1, 1, 2, 4, 8], maxlen=6)
    while True:
        yield q[0]
        q.append(q[-1] * 2 - q[0])
        
def count_odd_pentaFib(n):
    return sum(1 for key, grp in groupby(islice(odd_penta_fib(), n+1)) if key % 2 == 1)
