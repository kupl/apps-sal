def operation(op1, op2, op):
    if op == "*":
        return op1 * op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    else:
        return op1 / op2


def calculate(expression):
    i, lst, num = 0, [], ""
    if "." in expression:
        if expression.replace(".", "").isdigit():
            return float(expression)
    while i < len(expression):
        if not expression[i].isdigit():
            if expression[i] in "+-*$":
                lst.append(int(num))
                lst.append(expression[i])
                num = ""
            else:
                return "400: Bad request"
        else:
            num += expression[i]
        i += 1
    if expression[i - 1].isdigit():
        lst.append(int(num))
    length = len(lst)
    while(True):
        if "*" in lst and "$" in lst:
            index1, index2 = lst.index('*'), lst.index('$')
            if index1 < index2 and index1 - 1 > -1 and index1 + 1 < length and (type(lst[index1 - 1]) == int or type(lst[index1 - 1]) == float) and (type(lst[index1 + 1]) == int or type(lst[index1 + 1]) == float):
                lst[index1 - 1] = operation(lst.pop(index1 - 1), lst.pop(index1), lst[index1 - 1])
            elif index2 - 1 > -1 and index2 + 1 < length and (type(lst[index2 - 1]) == int or type(lst[index2 - 1]) == float) and (type(lst[index2 + 1]) == int or type(lst[index2 + 1]) == float):
                lst[index2 - 1] = operation(lst.pop(index2 - 1), lst.pop(index2), lst[index2 - 1])
            else:
                return "400: Bad request"
        elif "*" in lst:
            index = lst.index("*")
            if index - 1 > -1 and index + 1 < length and (type(lst[index - 1]) == int or type(lst[index - 1]) == float) and (type(lst[index + 1]) == int or type(lst[index + 1]) == float):
                lst[index - 1] = operation(lst.pop(index - 1), lst.pop(index), lst[index - 1])
            else:
                return "400: Bad request"
        elif "$" in lst:
            index = lst.index("$")
            if index - 1 > -1 and index + 1 < length and (type(lst[index - 1]) == int or type(lst[index - 1]) == float) and (type(lst[index + 1]) == int or type(lst[index + 1]) == float):
                lst[index - 1] = operation(lst.pop(index - 1), lst.pop(index), lst[index - 1])
            else:
                return "400: Bad request"
        elif "+" in lst and "-" in lst:
            index1, index2 = lst.index('+'), lst.index('-')
            if index1 < index2 and index1 - 1 > -1 and index1 + 1 < length and (type(lst[index1 - 1]) == int or type(lst[index1 - 1]) == float) and (type(lst[index1 + 1]) == int or type(lst[index1 + 1]) == float):
                lst[index1 - 1] = operation(lst.pop(index1 - 1), lst.pop(index1), lst[index1 - 1])
            elif index2 - 1 > -1 and index2 + 1 < length and (type(lst[index2 - 1]) == int or type(lst[index2 - 1]) == float) and (type(lst[index2 + 1]) == int or type(lst[index2 + 1]) == float):
                lst[index2 - 1] = operation(lst.pop(index2 - 1), lst.pop(index2), lst[index2 - 1])
            else:
                return "400: Bad request"
        elif "+" in lst:
            index = lst.index("+")
            if index - 1 > -1 and index + 1 < length and (type(lst[index - 1]) == int or type(lst[index - 1]) == float) and (type(lst[index + 1]) == int or type(lst[index + 1]) == float):
                lst[index - 1] = operation(lst.pop(index - 1), lst.pop(index), lst[index - 1])
            else:
                return "400: Bad request"
        elif "-" in lst:
            index = lst.index("-")
            if index - 1 > -1 and index + 1 < length and (type(lst[index - 1]) == int or type(lst[index - 1]) == float) and (type(lst[index + 1]) == int or type(lst[index + 1]) == float):
                lst[index - 1] = operation(lst.pop(index - 1), lst.pop(index), lst[index - 1])
            else:
                return "400: Bad request"
        else:
            break
    return lst.pop()
