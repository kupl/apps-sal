def max_tri_sum(numbers):
    n=list(set(numbers))
    n.sort(reverse=1)
    return sum(n[:3])
