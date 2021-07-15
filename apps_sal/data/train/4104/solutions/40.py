def max_tri_sum(numbers):
    new_n=list(set(numbers))
    r1=max(new_n)
    new_n.remove(r1)
    r2=max(new_n)
    new_n.remove(r2)
    r3=max(new_n)
    new_n.remove(r3)
    return r1+r2+r3

