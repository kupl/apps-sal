def solve(st):
    left_index = dict()
    right_index = dict()
    
    for i, c in enumerate(st):
        right_index[c] = i
    for i, c in reversed(list(enumerate(st))):
        left_index[c] = i
        
    return max((right_index[c] - left_index[c], -ord(c), c) for c in set(st))[2]
