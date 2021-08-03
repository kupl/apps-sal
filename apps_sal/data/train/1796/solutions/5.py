def to_postfix(infix):
    postfix = ""
    rop = []
    priority = []
    for i, d in enumerate(infix):
        if d in "0123456789":
            postfix += d
        elif d == "(":
            priority.append(len(rop))
        elif d == ")":
            priority.pop()
            postfix += rop.pop()
        else:
            if len(rop) > 0 and (len(priority) == 0 or len(rop) > priority[-1]):
                if d in "+-":
                    postfix += "".join(rop[::-1])
                    rop = []
                elif rop[-1] in "*/^":
                    postfix += rop.pop()
            rop.append(d)
    return postfix + "".join(rop[::-1])
