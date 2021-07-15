from itertools import chain

def hyperrectangularity_properties(arr):
    hr, arr = [], [arr]
    while 1:
        check = sum(isinstance(v, int) for v in arr)        # Check homogeneity
        if check or not arr:                                # some int are present or empty array (edge case)
            if check == len(arr): return tuple(hr)          # only int: found the bottom of the tree
            break
            
        l = set(map(len,arr))
        if len(l) > 1: break                                # invalid if different length found
        hr.append(l.pop())
        arr = list(chain.from_iterable(arr))                # get the "lower level"
