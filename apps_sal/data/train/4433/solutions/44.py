def logical_calc(array, op):
    if len(array)==1:
        return array[0]
    else:
        if op.lower()=='and':
            s=array[0] & array[1]
            for i in range(2,len(array)):
                s=s & array[i]
            return s
        elif op.lower()=='or':
            s=array[0] | array[1]
            for i in range(2,len(array)):
                s=s | array[i]
            return s
        if op.lower()=='xor':
            s=array[0] ^ array[1]
            for i in range(2,len(array)):
                s=s ^ array[i]
            return s
