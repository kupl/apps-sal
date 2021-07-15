# Solution 1
def digits(num):
    return [int(a)+int(b) for i,a in enumerate(str(num)) for b in str(num)[(i+1):]]
    
    
# Solution 2
def digits(num):
    from itertools import combinations
    return [int(a)+int(b) for a,b in combinations(str(num), 2)]
