from collections import defaultdict, deque
import re

def replace(s):
    chunks = re.findall(r'!+|\?+', s)
    cnts   = defaultdict(deque)
    for i,c in enumerate(chunks[:]):
        other = '!?'[c[0]=='!'] * len(c)
        if cnts[other]:
            blank = ' '*len(c)
            chunks[i] = chunks[cnts[other].popleft()] = blank
        else:
            cnts[c].append(i)
    
    return ''.join(chunks)
