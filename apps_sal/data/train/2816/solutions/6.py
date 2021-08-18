def calculate(s):
    t = s.replace("plus", "+")
    y = t.replace("minus", "-")
    return str(eval(y))
