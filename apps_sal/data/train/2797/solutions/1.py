def mobile_keyboard(s):
    return sum((x+1) for x in range(5) for c in s if c in ['0123456789*#','adgjmptw','behknqux','cfilorvy','sz'][x])

