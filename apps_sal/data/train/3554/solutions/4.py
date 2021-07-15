#List Comprehensions is so powerful
from itertools import groupby
def get_score(a): 
    s = 0
    if set(a)==set([1,2,3,4,5,6]): s=1000  #Straight
    else:
        if len(set([i*10 if i==1 else i for i in a if a.count(i)==2]))==3: s=750 #Three pairs
        else:
            s+=sum(sum(set([i*10 if i==1 else i for i in a if a.count(i)==k]))*100*(k-2) for k in (3,4,5,6)) #Three-four-five-six
            s+=sum((i*10 if i==1 else i)*a.count(i) for i in (1,5) if a.count(i) in (1,2))*10 # Every 1 and 5
    return s if s!=0 else "Zonk"
