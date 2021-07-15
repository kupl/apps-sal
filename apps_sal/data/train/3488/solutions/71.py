def eval_object(v):
    if v['operation'] == "+":
        return v['a']+v['b']
    if v['operation'] == "-":
        return v['a']-v['b']
    if v['operation'] == "*":
        return v['a']*v['b']
    if v['operation'] == "/":
        return v['a']/v['b']
    if v['operation'] == "**":
        return v['a']**v['b']
    if v['operation'] == "%":
        return v['a']%v['b']
