def largest_pair_sum(num): 
    return num.pop(num.index(max(num))) + max(num)
