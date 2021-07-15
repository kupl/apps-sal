def logical_calc(array, op):
    op = op.lower()
    if op == "xor":
        op = "!="
    for id in range(len(array)-1):
        array[id+1]=eval(str(array[id])+" "+op+" "+str(array[id+1]))
    return array[-1]#boolean
