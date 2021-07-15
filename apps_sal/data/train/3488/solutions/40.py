def eval_object(v):
    """return {"+": v['a']+v['b'],
        "-": v['a']-v['b'],
        "/": v['a']/v['b'],
        "*": v['a']*v['b'],
        "%": v['a']%v['b'],
        "**": v['a']**v['b'], }.get('operation',1)"""
    if v.get("operation") == "+":
        return v.get("a") + v.get("b")
    elif v.get("operation") == "-":
        return v.get("a") - v.get("b")
    elif v.get("operation") == "/":
        try:
            return v.get("a") / v.get("b")
        except ZeroDivisionError:
            return "Can't divide by Zero"
    elif v.get("operation") == "*":
        return v.get("a") * v.get("b")
    elif v.get("operation") == "%":
        return v.get("a") % v.get("b")
    elif v.get("operation") == "**":
        return v.get("a") ** v.get("b")
