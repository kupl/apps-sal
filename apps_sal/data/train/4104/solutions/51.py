def max_tri_sum(numbers):
    lst = list(set(numbers))
    lst.sort()

    return sum(lst[-1:-4:-1])
