from itertools import combinations as c
def find_zero_sum_groups(a,n):
    if not len(a):return 'No elements to combine'
    r=[sorted(x) for x in c(sorted(set(a)),n) if sum(x)==0]
    return sorted(r) if len(r)>1 else r[0] if len(r) else 'No combinations'
