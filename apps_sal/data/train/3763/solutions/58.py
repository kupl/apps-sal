def calculator(x,y,op):
    ops = {'+':add,'-':sub,'*':mul,'/':div}
    try:
        return ops[op](x,y)
    except KeyError:
        return 'unknown value'

def add(num1,num2):
    try:
        return float(num1)+float(num2)
    except:
        return 'unknown value'

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2
