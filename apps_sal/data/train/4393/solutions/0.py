from collections import defaultdict

def repeat_sum(l):
    count = defaultdict(int)
    for l1 in l:
        for val in set(l1):
            count[val] += 1
    
    return sum(k for k,v in list(count.items()) if v > 1)

