def sum_to_infinity(l):
    return round(l[0]/(1- l[1]/l[0]),3) if l[1]/l[0] < 1 and l[1]/l[0] > -1 else 'No Solutions'
