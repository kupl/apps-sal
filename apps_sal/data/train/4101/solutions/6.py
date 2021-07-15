from decimal import *

def sum_prod(strexpression):
    splitByPlus = strexpression.split("+")
    for x in range(0, len(splitByPlus)):
        splitByPlus[x] = multiplyAll(splitByPlus[x])
    result = addAll(splitByPlus);
    return "{:.5e}".format(result);
        
def addAll(exps):
    sum = 0.0
    for i in exps: 
        sum += float(i);
    return sum;
    
def multiplyAll(exps):
    exps = exps.split("*")
    result = 1.0
    for j in exps: 
        result *= float(j);
    return result;
