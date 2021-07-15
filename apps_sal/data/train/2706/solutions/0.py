def pass_the_bill(total, conservative, reformist):
    ind = total - conservative - reformist
    majority = total//2 + 1
    if conservative > majority:
        return 0
    elif conservative + ind < majority:
        return -1
    else:
        return majority - conservative
