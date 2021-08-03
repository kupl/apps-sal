def calculate(s):
    ret = eval(s.replace("plus", "+").replace("minus", "-"))
    return str(ret)
