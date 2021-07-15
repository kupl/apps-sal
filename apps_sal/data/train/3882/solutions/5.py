import itertools
def sort_by_value_and_index(nums):
    #your code here
    seq = itertools.count(1)
    return sorted(nums, key=lambda num:num*next(seq))
