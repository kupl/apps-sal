def index_numbers(a, b, c, d):
    lst = [a,b,c,d]
    for i in lst:
        lst1 = lst[:]
        lst1.remove(i)
        for j in lst1:
            lst2 = lst1[:]
            lst2.remove(j)
            for k in lst2:
                lst3 = lst2[:]
                lst3.remove(k)
                for l in lst3:
                    yield [i,j,k,l]

def index_symbols():
    lst = ['+', '-', '*', '/']
    for i in lst:
        for j in lst:
            for k in lst:
                yield [i,j,k]
            
def evaluate0(num, sym):
    expr = num[0] + sym[0] + num[1] + sym[1] + num[2] + sym[2] + num[3]
    try:
        res = eval(expr)
    except:
        res = 0
    return res, expr

def evaluate1(num, sym):
    expr = '(' + num[0] + sym[0] + num[1] + sym[1] + num[2] + ')' + sym[2] + num[3]
    try:
        res = eval(expr)
    except:
        res = 0
    return res, expr

def evaluate2(num, sym):
    expr = '(' + num[0] + sym[0] + num[1]  + ')' + sym[1] + '(' + num[2] + sym[2] + num[3] + ')'
    try:
        res = eval(expr)
    except:
        res = 0
    return res, expr

def evaluate3(num, sym):
    expr = num[0] + sym[0]  + '(' + num[1] + sym[1] + '(' + num[2] + sym[2] + num[3] + "))"
    try:
        res = eval(expr)
    except:
        res = 0
    return res, expr

def evaluate4(num, sym):
    expr = "((" +num[0] + sym[0] + num[1] + ')' + sym[1] + num[2] + ')' + sym[2] + num[3]
    try:
        res = eval(expr)
    except:
        res = 0
    return res, expr

def equal_to_24(a,b,c,d):

    for num in index_numbers(str(a), str(b), str(c), str(d)):
        for sym in index_symbols():
        
            val, text = evaluate0(num, sym) 
            if  val == 24:
                return text
            
            val, text = evaluate1(num, sym) 
            if  val == 24:
                return text
    
            val, text = evaluate2(num, sym) 
            if  val == 24:
                return text
            
            val, text = evaluate3(num, sym) 
            if  val == 24:
                return text
            
            val, text = evaluate4(num, sym) 
            if  val == 24:
                return text
            
    return "It's not possible!"
