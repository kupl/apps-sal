def calculator(x,y,op):
    if op in ['+','-','*','/']:
        try:
            return {'+':x+y,'-':x-y,'*':x*y,'/':x/y}[op]
        except TypeError:
            return 'unknown value'
    else: return 'unknown value'
