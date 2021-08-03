def max_tri_sum(n):
    # your code here
    n = list(set(n))
    n.sort(reverse=True)
    return sum(n[0:3])
