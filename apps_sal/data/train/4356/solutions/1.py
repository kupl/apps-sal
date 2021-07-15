from functools import reduce
from collections import Counter

def colorful(n):
    s = list(map(int,str(n)))
    cnt = Counter( reduce(int.__mul__, s[i:i+x]) for x in range(1,len(s)+1) for i in range(len(s)-x+1))
    return cnt.most_common(1)[0][1] == 1
