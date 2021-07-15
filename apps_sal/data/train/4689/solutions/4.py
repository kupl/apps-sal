from collections import Counter
from itertools import chain

def create_report(names):
    if any(name.startswith("Labrador Duck ") for name in names): return ["Disqualified data"]
    counts = Counter()
    for name,count in (d.rsplit(None, 1) for d in names):
        counts[code(name)] += int(count)
    return list(chain(*sorted(counts.items())))

def code(name):
    words = name.upper().replace("-"," ").split(None, 3)  # Generate at most 4 words
    lengths = [ (6,), (3,3), (2,2,2), (1,1,2,2) ][len(words)-1]
    return "".join(word[:lengths[i]] for i,word in enumerate(words))
