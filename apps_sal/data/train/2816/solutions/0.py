def calculate(s):
    return str(sum(int(n) for n in s.replace("minus", "plus-").split("plus")))
