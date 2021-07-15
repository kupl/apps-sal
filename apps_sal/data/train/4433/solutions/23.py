def logical_calc(array, op):
    if op=='AND': return all(array)
    elif op=='OR': return any(array)
    else: return sum(array)%2==1
