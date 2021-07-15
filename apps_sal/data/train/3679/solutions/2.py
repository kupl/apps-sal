def calculate_string(st):
    clean = ""
    for i in st:
        if i.isdigit() or i == ".":
            clean += i
        elif i in ["+","-","*","/"]:
            clean += i
            operator = i
    clean = clean.split(operator)
    print(clean)
    if operator == "+":
        return str(round(float(clean[0])+float(clean[1])))
    elif operator == "-":
        return str(round(float(clean[0])-float(clean[1])))
    elif operator == "*":
        return str(round(float(clean[0])*float(clean[1])))
    else:
        return str(round(float(clean[0])/float(clean[1])))
