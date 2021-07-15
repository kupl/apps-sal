from collections import Counter
from math import gcd
def has_subpattern(string):
    temp=Counter(string)
    if temp.most_common(1)[0][1]==1:
        return False
    res=sorted(temp.items(), key=lambda x:x[1])
    if len(res)==1:
        return True
    check=res[-1][1]
    for i in range(1, len(res)):
        check=min(check, gcd(res[i][1], res[i-1][1]))
    if check==1:
        return False
    for i in res:    
        if i[1]%check!=0:
            return False
    return True
