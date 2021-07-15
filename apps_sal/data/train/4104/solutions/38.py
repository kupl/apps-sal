def max_tri_sum(numbers):
    lst=[i for i in sorted(set(numbers),reverse = True)]
    return sum(lst[:3])
