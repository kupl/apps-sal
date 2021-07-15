def calculate(s):
    # your code here
    t=s.replace("plus","+")
    y=t.replace("minus","-")
    #print(y)
    return str(eval(y))

