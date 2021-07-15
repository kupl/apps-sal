from collections import Counter
from itertools import chain

def crap(garden, bags, cap):
    c = Counter(chain(*garden))
    return 'Dog!!' if c['D'] else ('Clean','Cr@p')[c['@'] > bags*cap]
