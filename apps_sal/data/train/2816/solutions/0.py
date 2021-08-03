def calculate(s):
    return str(sum(int(n) for n in s.replace("minus", "plus-").split("plus")))

    # I heard here and there that using eval is a very bad practice…
    # return str(eval(s.replace("plus", "+").replace("minus", "-")))
