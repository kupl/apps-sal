def est_subsets(arr):
    # your code here
    return 2**len(set(arr)) - 1   # n: amount of subsets that do not have repeated elements 
