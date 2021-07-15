def est_subsets(arr):
    # your code here

    s = set(arr)

    return 2**(len(s)) - 1   # n: amount of subsets that do not have repeated elements 
