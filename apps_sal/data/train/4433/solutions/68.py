def logical_calc(array, op):
    logic = ""
    if op == "XOR":
        op = "^"
    
    for x in array[0:len(array)-1]:
        logic = logic + " " + str(x) + " " + op.lower()
    
    logic = logic + " " + str(array[-1])
    
    ans = eval(logic.strip())
    
    return ans
