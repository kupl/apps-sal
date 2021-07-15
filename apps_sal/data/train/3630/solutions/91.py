def arithmetic(a, b, operator):
    result=0
    if operator=="add":
        result=a+b
        return result
    elif operator=="subtract":
        result=a-b
        return result
    elif operator=="multiply":
        result=a*b
        return result
    else:
        result=a/b
        return result

