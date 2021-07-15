def basic_op(operator, value1, value2):
    #your code here
    if operator == "+":
        answer = int(value1) + int(value2)
    elif operator == "-":
        answer = int(value1) - int(value2)
    elif operator == "*":
        answer = int(value1) * int(value2)
    else:
        answer = int(value1) / int(value2)
    return answer
