def max_tri_sum(numbers):
    a = set(numbers)
    b = max(a)
    c = a.remove(b)
    d = max(a)
    e = a.remove(d)
    f = max(a)
    return b + d + f
    # your code here
