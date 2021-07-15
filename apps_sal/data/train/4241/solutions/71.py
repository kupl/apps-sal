def sequence_sum(a, b, d):
    if a <= b:
        return sum(range(a,b+1,d))
    else:
        return 0
