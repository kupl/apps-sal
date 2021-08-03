def max_tri_sum(numbers):
    # your code here
    n = list(set(numbers))
    n.sort(reverse=True)
    return sum(n[:3])
