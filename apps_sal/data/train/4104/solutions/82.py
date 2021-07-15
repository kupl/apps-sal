def max_tri_sum(numbers):
    setnumber = sorted(set(numbers))
    return sum(setnumber[-3:])
