def are_equally_strong(l1, r1, l2, r2):
    return max(l1, r1) == max(l2, r2) and min(l1, r1) == min(l2, r2)
