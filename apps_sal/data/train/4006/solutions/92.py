def basic_op(operator, value1, value2):
    anwser=0
    if operator == "+":
        anwser = value1+value2
    elif operator == "-":
        anwser = value1-value2
    elif operator == "*":
        anwser = value1*value2
    elif operator == "/":
        anwser = value1/value2
    return anwser
