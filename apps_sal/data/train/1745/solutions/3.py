from operator import truediv, mul, sub, add
operators = {'/':truediv,'*':mul,'+':add,'-':sub}
order = [{'/', '*'}, {'-', '+'}]
    
def calculate(expression):
    expression = expression.replace('$','/') 
    for i in '+*/-':
        expression = expression.replace(i,' '+i+' ')
    l = expression.split()
    try:
        for i in range(2):
            n = 0
            while n < len(l):
                if l[n] in order[i]:
                    l[n-1] = operators[l[n]](float(l.pop(n-1)),float(l.pop(n)))
                else:n+=1   
        return float(l[0])
    except:
        return '400: Bad request'
