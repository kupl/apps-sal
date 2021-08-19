def max_tri_sum(numbers):
    # returns the maximum value of the three highest integers
    # given in an array without duplication while summing.
    return sum(sorted(set(numbers), reverse=True)[0:3])
