from itertools import combinations as cb
def is_onion_array(a):
    return not any([sum(c) == len(a)-1 and a[c[0]]+a[c[1]] > 10 for c in cb([*range(0,len(a))],2)])
