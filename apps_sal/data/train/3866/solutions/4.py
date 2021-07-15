def isValidCnd(c):
    return all(k in c for k in ('name','scores')) and 0<len(c['scores'])<3 and all(not v%5 and 0<v<=100 for v in c['scores'])

def winner(cnds):
    if len(cnds) != 3 or not all(isValidCnd(c) for c in cnds): 
        return False
    return max(( (sum(c['scores']),-i,c['name']) for i,c in enumerate(cnds) if 0<=sum(c['scores'])<=100), default=(0,0,False))[2]
