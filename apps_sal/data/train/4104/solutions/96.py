from itertools import combinations
def max_tri_sum(numbers):
    #your code here
    return max([sum(x) for x in list(combinations(set(numbers), 3))]) 
