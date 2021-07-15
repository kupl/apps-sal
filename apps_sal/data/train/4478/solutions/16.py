def sum_to_infinity(sequence):
    r=sequence[1]/sequence[0]
    return round(sequence[0]/(1-r),3) if abs(r)<1 else 'No Solutions'
