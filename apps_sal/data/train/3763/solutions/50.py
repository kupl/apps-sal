def calculator(x,y,op):
    print(op)
    print((x,y))
    if type(x)!= int or type(y) != int:
        return 'unknown value'
    if op =='+':
            return x + y
    elif op =='-':
        return x - y
    elif op =='*':
           return x * y
    elif op =='/':
           return x / y
#     elif op =='&':
    else:
        return 'unknown value'

