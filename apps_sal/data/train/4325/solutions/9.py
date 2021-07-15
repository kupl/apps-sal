def knight_rescue(ns,x,y):
    return any(n%2==0 or n>0 and x%2==y%2 for n in ns)
