def calculate(num1, oper, num2): 
    return None if all((oper=='/',num2==0)) else {
            '+':lambda x,y:x+y,
            '-':lambda x,y:x-y,
            '/':lambda x,y:x/y,
            '*':lambda x,y:x*y,}.get(oper, lambda x,y:None)(num1,num2)

