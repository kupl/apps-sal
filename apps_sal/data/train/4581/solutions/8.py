from collections import Counter
def are_similar(a,b):
    return (len(a)-sum(v1==v2 for v1,v2 in zip(a,b))) in {0,2} and Counter(a)==Counter(b)
