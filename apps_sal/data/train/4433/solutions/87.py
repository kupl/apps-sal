def logical_calc(ar, op):
    if op == 'AND':
        return (False not in ar)
    elif op == 'OR':
        return (True in ar)
    elif op == 'XOR':
        if len(ar) == 2:
            return not (ar[0] == ar[1])
        elif len(ar) > 2:
            a = ar.pop(0)
            b = ar.pop(0)
            ar.insert(0,not (a == b))
            return logical_calc(ar, op)
        elif len(ar) == 1:
            return ar[0]
